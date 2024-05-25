from flask import Flask, request, redirect, url_for, session, render_template, jsonify, make_response
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
app.config["MYSQL_PASSWORD"] = "santos"
app.config["MYSQL_DB"] = "enrollment"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        email = request.form['email']
        first_name = request.form['first_name']
        middle_initial = request.form['middle_initial']
        last_name = request.form['last_name']
        date_of_birth = request.form['date_of_birth']
        address = request.form['address']
        city = request.form['city']
        country = request.form['country']
        postal_code = request.form['postal_code']
        phone_number = request.form['phone_number']
        
        cursor = mysql.connection.cursor()
        cursor.execute('''
            INSERT INTO users (username, password, email, first_name, middle_initial, last_name, date_of_birth, address, city, country, postal_code, phone_number)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (username, password, email, first_name, middle_initial, last_name, date_of_birth, address, city, country, postal_code, phone_number))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        cursor.close()
        
        if user:
            session['username'] = user['username']
            return redirect(url_for('profile')) 
        else:
            return 'Invalid username or password'
    
    return render_template('login.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' in session:
        if request.method == 'GET':
            username = session['username']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            user = cursor.fetchone()
            
            # Fetch enrolled students with their course details
            cursor.execute('''
                SELECT users.username, users.email, users.first_name, users.last_name, courses.name AS course_name
                FROM users
                INNER JOIN enrollments ON users.username = enrollments.username
                INNER JOIN courses ON enrollments.course_id = courses.id
            ''')
            enrolled_students = cursor.fetchall()
            
            cursor.close()
            return render_template('profile.html', user=user, enrolled_students=enrolled_students)
        elif request.method == 'POST':
            # Example: Update user information
            new_first_name = request.form['first_name']
            new_last_name = request.form['last_name']
            # Update user information in the database
            cursor = mysql.connection.cursor()
            cursor.execute('UPDATE users SET first_name = %s, last_name = %s WHERE username = %s', (new_first_name, new_last_name, session['username']))
            mysql.connection.commit()
            cursor.close()

if __name__ == '__main__':
    app.run(debug=True)
