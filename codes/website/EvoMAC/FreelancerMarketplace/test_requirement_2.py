'''
Test whether the first page of the website is the login page and whether it can log in correctly based on the example data provided in the Task.
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class TestFreelancerMarketplaceLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")
    def test_login_page(self):
        driver = self.driver
        # Check if the current page is the login page
        self.assertIn("Login", driver.title)
        print("Login page title is correct.")
        # Locate username and password fields
        username_field = driver.find_element(By.ID, "username_field")
        password_field = driver.find_element(By.ID, "password_field")
        login_button = driver.find_element(By.ID, "login_button")
        # Input example data
        username = "john_doe"
        password = "securePassword123"
        username_field.send_keys(username)
        password_field.send_keys(password)
        # Click the login button
        login_button.click()
        # Wait for the page to load
        time.sleep(2)
        # Check if redirected to Home Page
        self.assertIn("Home", driver.title)
        print("Successfully logged in and redirected to Home page.")
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()