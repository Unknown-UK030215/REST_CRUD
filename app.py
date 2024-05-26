from flask import Flask, request, redirect, url_for, session, jsonify, make_response, render_template, flash, Response
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

# CREATE operation (User Registration)
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
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('''
            INSERT INTO users (username, password, email, first_name, middle_initial, last_name, date_of_birth, address, city, country, postal_code, phone_number)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (username, password, email, first_name, middle_initial, last_name, date_of_birth, address, city, country, postal_code, phone_number))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route("/", methods=["GET", "POST"])
def login():
    msg = ''
    if request.method == "POST" and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, hashed_password,))
        account = cursor.fetchone()
        cursor.close()

        if account:
            session['loggedin'] = True
            session['user_id'] = account['user_id']
            session['username'] = account['username']
            return redirect(url_for('profile'))
        else:
            msg = 'Invalid username or password'
    
    return render_template('login.html', msg=msg)

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
                INNER JOIN courses ON enrollments.course_id = courses.course_id
            ''')
            enrolled_students = cursor.fetchall()
            
            cursor.close()
            return render_template('profile.html', user=user, enrolled_students=enrolled_students)
        
        elif request.method == 'POST':
            # Retrieve form data
            course_id = request.form['course_id']
            username = session['username']
            grade = None
            status = 'active'
            
            # Enroll the user in the selected course
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('''
                INSERT INTO enrollments (username, course_id, grade, status)
                VALUES (%s, %s, %s, %s)
            ''', (username, course_id, grade, status))
            mysql.connection.commit()
            cursor.close()
            
            # Redirect the user back to the profile page
            return redirect(url_for('profile'))
    
    # Redirect users to the login page if they're not logged in
    return redirect(url_for('login'))

@app.route('/download_user/<string:format>')
def download_user(format):
    if 'username' in session:  # Check if user is logged in
        username = session['username']  # Retrieve username from session
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # Fetch user data for the logged-in user
        cursor.execute('''
            SELECT * FROM users WHERE username = %s
        ''', (username,))
        user_data = cursor.fetchone()  # Fetch the user's data
        cursor.close()

        # Check the requested format (JSON or XML)
        if format == 'json':
            # Convert user data to JSON format
            response = jsonify(user_data)
            response.headers.set('Content-Disposition', 'attachment', filename='user_data.json')
            return response
        elif format == 'xml':
            # Convert user data to XML format
            root = Element('User')
            for key, value in user_data.items():
                SubElement(root, key).text = str(value)
            response = Response(tostring(root, encoding='unicode'), mimetype='application/xml')
            response.headers.set('Content-Disposition', 'attachment', filename='user_data.xml')
            return response

    # If user is not logged in, redirect to the login page
    return redirect(url_for('login'))


@app.route('/view_users')
def view_users():
    # Fetch users from the database
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()

    return render_template('view_users.html', users=users)

@app.route('/edit_user/<string:username>', methods=['GET', 'POST'])
def edit_user(username):
    if request.method == 'POST':
        new_email = request.form['email']
        new_first_name = request.form['first_name']
        new_last_name = request.form['last_name']
        new_middle_initial = request.form['middle_initial']
        new_date_of_birth = request.form['date_of_birth']
        new_address = request.form['address']
        new_city = request.form['city']
        new_country = request.form['country']
        new_postal_code = request.form['postal_code']
        new_phone_number = request.form['phone_number']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('''
            UPDATE users
            SET email = %s, first_name = %s, last_name = %s, middle_initial = %s, date_of_birth = %s,
                address = %s, city = %s, country = %s, postal_code = %s, phone_number = %s
            WHERE username = %s
        ''', (new_email, new_first_name, new_last_name, new_middle_initial, new_date_of_birth,
              new_address, new_city, new_country, new_postal_code, new_phone_number, username))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('view_users'))

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user = cursor.fetchone()
    cursor.close()
    return render_template('edit_user.html', user=user)



# Route for deleting a user
@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    # Connect to MySQL and delete the user from the database
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
    mysql.connection.commit()
    cur.close()

    # Redirect back to the view_users route
    return redirect(url_for('view_users'))



@app.route('/courses', methods=['GET', 'POST'])
def courses():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        description = request.form['description']
        instructor = request.form['instructor']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        location = request.form['location']
        max_capacity = request.form['max_capacity']
        fee = request.form['fee']

        # Save the course data to the database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('''
            INSERT INTO courses (name, description, instructor, start_date, end_date, location, max_capacity, fee)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (name, description, instructor, start_date, end_date, location, max_capacity, fee))
        mysql.connection.commit()
        cursor.close()

        # Redirect the user back to the courses page
        return redirect(url_for('courses'))
    
    # If it's a GET request, just render the courses template
    return render_template('courses.html')




@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    if request.method == 'GET':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM courses')
        courses = cursor.fetchall()
        cursor.close()
        return render_template('enroll.html', courses=courses)
    elif request.method == 'POST':
        course_id = request.form['course_id']
        username = session['username']
        grade = None
        status = 'active'
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('''
            INSERT INTO enrollments (username, course_id, grade, status)
            VALUES (%s, %s, %s, %s)
        ''', (username, course_id, grade, status))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('profile'))



@app.route('/enrolled_courses', methods=['GET', 'POST'])
def enrolled_courses():
    if 'username' in session:
        username = session['username']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('''
            SELECT courses.course_id, courses.name, courses.description, courses.instructor, courses.start_date, courses.end_date, courses.location, enrollments.grade
            FROM courses
            INNER JOIN enrollments ON courses.course_id = enrollments.course_id
            WHERE enrollments.username = %s
        ''', (username,))
        enrolled_courses = cursor.fetchall()
        cursor.close()

        return render_template('enrolled_courses.html', enrolled_courses=enrolled_courses)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


# New API endpoint for course information
class CourseAPI(Resource):
    def get(self, course_id):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM courses WHERE id = %s', (course_id,))
        course = cursor.fetchone()
        cursor.close()
        if course:
            return jsonify(course)
        return make_response(jsonify({'error': 'Course not found'}), 404)

# New API endpoint for user enrollment information
class UserEnrollmentAPI(Resource):
    def get(self, username):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('''
            SELECT courses.name, courses.description
            FROM courses
            INNER JOIN enrollments ON courses.course_id = enrollments.course_id
            WHERE enrollments.username = %s
        ''', (username,))
        enrolled_courses = cursor.fetchall()
        cursor.close()
        if enrolled_courses:
            return jsonify(enrolled_courses)
        return make_response(jsonify({'error': 'No courses enrolled'}), 404)


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
api.add_resource(CourseAPI, '/api/course/<int:course_id>')
api.add_resource(UserEnrollmentAPI, '/api/enrollment/<string:username>')

if __name__ == '__main__':
    app.run(debug=True)
