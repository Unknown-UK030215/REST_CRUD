import unittest
import warnings
from  app import app
import api  # Add this line to import the api module

class MyAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_register(self):
        new_user_data = {
            "username": "test_user",
            "password": "test_password",
            "email": "test@example.com",
            "first_name": "Test",
            "middle_initial": "M",
            "last_name": "User",
            "date_of_birth": "1990-01-01",
            "address": "123 Test St",
            "city": "Testville",
            "country": "Testland",
            "postal_code": "12345",
            "phone_number": "123-456-7890"
        }
        response = self.app.post("/register", data=new_user_data)
        self.assertEqual(response.status_code, 302)  # Assuming registration redirects to login page

    def test_login(self):
        login_data = {"username": "test_user", "password": "test_password"}
        response = self.app.post("/", data=login_data)
        self.assertEqual(response.status_code, 302)  # Assuming successful login redirects to profile page

    def test_profile(self):
        response = self.app.get("/profile")
        self.assertEqual(response.status_code, 302)  # Assuming redirects to login page if not logged in

    def test_download_user_json(self):
        response = self.app.get("/download_user/json")
        self.assertEqual(response.status_code, 302)  # Assuming redirects to login page if not logged in

    def test_download_user_xml(self):
        response = self.app.get("/download_user/xml")
        self.assertEqual(response.status_code, 302)  # Assuming redirects to login page if not logged in

    # Add more test cases as needed for other routes and functionalities

if __name__ == "__main__":
    unittest.main()
