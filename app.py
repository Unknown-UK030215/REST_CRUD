from flask import Flask, request, redirect, url_for, session, render_template_string, jsonify, make_response
from flask_mysqldb import MySQL
import hashlib
import os
from flask_restful import Resource, Api
import MySQLdb.cursors
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

app = Flask(__name__, template_folder='templates')
api = Api(app)
app.secret_key = os.urandom(24)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "giana"
app.config["MYSQL_DB"] = "enrollment"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
        mysql.connection.commit()
        cursor.close()
        
        return redirect(url_for('login'))
    
    return render_template_string('''
        <form method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Register</button>
        </form>
    ''')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        cursor.close()
        
        if user:
            session['username'] = user['username']
            return redirect(url_for('profile'))
        else:
            return 'Invalid username or password'
    
    return render_template_string('''
        <form method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
    ''')

@app.route('/profile')
def profile():
    if 'username' in session:
        return f"Logged in as {session['username']}"
    return redirect(url_for('login'))

class UserAPI(Resource):
    def get(self, username):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        cursor.close()
        
        if user:
            user_xml = Element('user')
            username_xml = SubElement(user_xml, 'username')
            username_xml.text = user['username']
            user_xml_str = tostring(user_xml)
            dom = parseString(user_xml_str)
            return app.response_class(dom.toxml(), content_type='application/xml')
        
        return make_response(jsonify({'error': 'User not found'}), 404)

api.add_resource(UserAPI, '/api/user/<string:username>')

if __name__ == '__main__':
    app.run(debug=True)
