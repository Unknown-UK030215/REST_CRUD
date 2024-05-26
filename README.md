# Flask Enrollment System

The Flask Enrollment System is a web application built using Flask, allowing users to register, login, enroll in courses, and interact with API endpoints to retrieve user and course information.

## Overview

The system provides a user-friendly interface for managing user registration, authentication, and course enrollment. Users can register with their details, log in securely, view their profile information, and enroll in available courses. Administrators can manage user accounts, course details, and view enrollment statistics.

## Setup

1. **Install Dependencies:** Ensure you have Python installed on your system. Then, install the required Python packages:

   ```bash
   pip install Flask Flask-MySQLdb flask-restful
   ```

2. **Database Setup:** Make sure you have MySQL installed and running. Create a MySQL database named `enrollment` and execute the following SQL queries to create the required tables:

   ```sql
   -- Table for storing user information
   CREATE TABLE users (
       user_id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) UNIQUE NOT NULL,
       password VARCHAR(255) NOT NULL,
       email VARCHAR(100) NOT NULL,
       first_name VARCHAR(50) NOT NULL,
       middle_initial VARCHAR(1),
       last_name VARCHAR(50) NOT NULL,
       date_of_birth DATE,
       address VARCHAR(255),
       city VARCHAR(50),
       country VARCHAR(50),
       postal_code VARCHAR(20),
       phone_number VARCHAR(20)
   );

   -- Table for storing course information
   CREATE TABLE courses (
       course_id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       description TEXT
   );

   -- Table for storing enrollments
   CREATE TABLE enrollments (
       enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) NOT NULL,
       course_id INT NOT NULL,
       grade VARCHAR(2),
       status VARCHAR(10) DEFAULT 'active',
       FOREIGN KEY (username) REFERENCES users(username),
       FOREIGN KEY (course_id) REFERENCES courses(course_id)
   );
   ```

3. **Configure Flask App:** In the `app.py` file, configure the Flask app with your MySQL credentials:

   ```python
   app.config["MYSQL_HOST"] = "localhost"
   app.config["MYSQL_USER"] = "your_username"
   app.config["MYSQL_PASSWORD"] = "your_password"
   app.config["MYSQL_DB"] = "enrollment"
   ```

4. **Run the Flask App:** Start the Flask app by running the following command:

   ```bash
   python app.py
   ```

## Usage

- **Registration:** Visit `/register` to register new users.
- **Login:** Access `/login` to log in to the system.
- **Profile:** Navigate to `/profile` to view user profile details.
- **Enrollment:** Go to `/enroll` to enroll in available courses.
- **Logout:** Visit `/logout` to log out from the system.

## API Endpoints

- **User API:** 
  - **Endpoint:** `/api/user/<username>` (GET)
  - **Description:** Retrieve user information by username.
  
- **Course API:** 
  - **Endpoint:** `/api/course/<course_id>` (GET)
  - **Description:** Retrieve course information by course ID.
  
- **User Enrollment API:** 
  - **Endpoint:** `/api/enrollment/<username>` (GET)
  - **Description:** Retrieve course enrollments for a specific user.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to submit issues or pull requests to enhance the project.
