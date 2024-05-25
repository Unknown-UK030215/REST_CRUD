### Enrollment Management System ###

### Overview ####
- The Enrollment Management System is a web application designed to manage user registrations, logins, and profiles with integration into a MySQL database. It allows users to register, log in, view and update their profiles, and see their enrolled courses.

### Features ###
- User Registration: Users can register by providing their personal details including username, password, email, and other personal information.

- User Login: Registered users can log in with their username and password.

- User Profile: Logged-in users can view their profile and update certain personal information.

- Enrolled Students List: Users can view a list of enrolled students along with the courses they are enrolled in.

### Technology Stack ###
- Backend Framework: Flask
- Database: MySQL
- Frontend: HTML templates (rendered using Flask's render_template method)
- APIs: RESTful API using flask_restful
- Session Management: Flask session


### Installation ###

1. Clone the repository:
- git clone https://github.com/Unknown-UK030215/REST_CRUD.git

- cd REST_CRUD

2. Create a virtual environment and activate it:
- python -m venv enrollment
- source enrollment/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the dependencies:
- pip install -r requirements.txt

4. Set up the MySQL database:

- Ensure you have MySQL installed and running.
- Create a database named enrollment.
- Run the following SQL script to create the required tables:

CREATE DATABASE enrollment;
USE enrollment;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(64) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    first_name VARCHAR(50),
    middle_initial CHAR(1),
    last_name VARCHAR(50),
    date_of_birth DATE,
    address VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100),
    postal_code VARCHAR(20),
    phone_number VARCHAR(20)
);

CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE enrollments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    course_id INT,
    FOREIGN KEY (username) REFERENCES users(username),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);


5. Configure the application:

Update the database configuration in app.py:
- app.config["MYSQL_HOST"] = "localhost"
- app.config["MYSQL_USER"] = "root"
- app.config["MYSQL_PASSWORD"] = "your_mysql_password"
- app.config["MYSQL_DB"] = "enrollment"

6. Run the application
- python app.py
- The application will be accessible at http://127.0.0.1:5000/.

### Usage ###
### Register ###
- Navigate to http://127.0.0.1:5000/register to access the registration page.

- Fill in the required details and submit the form to 
create a new account.

### Login ###
- Navigate to http://127.0.0.1:5000/ to access the login page.
- Enter your username and password to log in.

### Profile ###
- Once logged in, you will be redirected to your profile page.
- Here, you can view and update your personal information.
- You can also see a list of students enrolled in various courses.

