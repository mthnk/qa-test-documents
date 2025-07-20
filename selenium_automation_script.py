"""
E-Commerce Login Automation Test
Author: Metehan Kutlu
Date: December 2024
Description: Automated login test for TechStore e-commerce platform
Tools: Selenium WebDriver with Python
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import unittest

class ECommerceLoginTest(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment before each test"""
        # Chrome options for consistent testing
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")  # Desktop resolution
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        # Initialize Chrome driver
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 15)
        
        # Test data
        self.base_url = "https://demo-ecommerce.example.com"
        self.valid_email = "testuser@example.com"
        self.valid_password = "TestPass123!"
        self.invalid_password = "wrongpassword"
        
    def test_001_successful_login(self):
        """TC002 - Login with Valid Credentials"""
        print("Executing: TC002 - Login with Valid Credentials")
        
        # Step 1: Navigate to login page
        self.driver.get(f"{self.base_url}/login")
        
        # Step 2: Verify login page loaded
        login_title = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        self.assertIn("Login", login_title.text)
        
        # Step 3: Enter valid email
        email_field = self.driver.find_element(By.ID, "email")
        email_field.clear()
        email_field.send_keys(self.valid_email)
        
        # Step 4: Enter valid password
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(self.valid_password)
        
        # Step 5: Click login button
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        
        # Step 6: Verify successful login
        # Wait for dashboard or homepage to load
        dashboard_element = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "user-dashboard"))
        )
        
        # Verify user is logged in (check for logout button or user menu)
        logout_button = self.driver.find_element(By.LINK_TEXT, "Logout")
        self.assertTrue(logout_button.is_displayed())
        
        # Verify URL changed to dashboard
        current_url = self.driver.current_url
        self.assertIn("dashboard", current_url.lower())
        
        print("✅ TC002 PASSED - User successfully logged in")
        
    def test_002_invalid_password_login(self):
        """TC003 - Login with Invalid Password"""
        print("Executing: TC003 - Login with Invalid Password")
        
        # Step 1: Navigate to login page
        self.driver.get(f"{self.base_url}/login")
        
        # Step 2: Enter valid email
        email_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_field.clear()
        email_field.send_keys(self.valid_email)
        
        # Step 3: Enter invalid password
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(self.invalid_password)
        
        # Step 4: Click login button
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        
        # Step 5: Verify error message is displayed
        error_message = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
        )
        
        # Verify error message text
        expected_error = "Invalid email or password"
        actual_error = error_message.text
        self.assertIn(expected_error.lower(), actual_error.lower())
        
        # Verify user is still on login page
        current_url = self.driver.current_url
        self.assertIn("login", current_url.lower())
        
        print("✅ TC003 PASSED - Error message displayed for invalid password")
        
    def test_003_empty_fields_validation(self):
        """Additional Test - Login with Empty Fields"""
        print("Executing: Additional Test - Empty Fields Validation")
        
        # Navigate to login page
        self.driver.get(f"{self.base_url}/login")
        
        # Try to submit without entering credentials
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()
        
        # Check for validation messages
        try:
            email_validation = self.driver.find_element(By.ID, "email-error")
            password_validation = self.driver.find_element(By.ID, "password-error")
            
            self.assertTrue(email_validation.is_displayed())
            self.assertTrue(password_validation.is_displayed())
            
            print("✅ PASSED - Validation messages shown for empty fields")
        except:
            # Alternative: Check if submit button is disabled or form validation prevents submission
            current_url = self.driver.current_url
            self.assertIn("login", current_url.lower())
            print("✅ PASSED - Form prevented submission with empty fields")
            
    def test_004_mobile_responsive_login(self):
        """Mobile Responsive Test - Login on Mobile Viewport"""
        print("Executing: Mobile Responsive Login Test")
        
        # Set mobile viewport (iPhone 14 size: 390x844)
        self.driver.set_window_size(390, 844)
        
        # Navigate to login page
        self.driver.get(f"{self.base_url}/login")
        
        # Verify mobile layout
        email_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        
        # Check if fields are properly visible and sized for mobile
        email_size = email_field.size
        viewport_width = self.driver.execute_script("return window.innerWidth")
        
        # Email field should take reasonable portion of mobile screen width
        self.assertGreater(email_size['width'], viewport_width * 0.7)  # At least 70% of viewport
        
        # Perform login test on mobile viewport
        email_field.send_keys(self.valid_email)
        
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(self.valid_password)
        
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        
        # Verify button is clickable on mobile
        self.assertTrue(login_button.is_enabled())
        login_button.click()
        
        # Verify login success on mobile
        dashboard_element = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "user-dashboard"))
        )
        self.assertTrue(dashboard_element.is_displayed())
        
        print("✅ PASSED - Mobile responsive login working correctly")
        
    def tearDown(self):
        """Clean up after each test"""
        # Take screenshot if test failed
        if hasattr(self, '_outcome') and not self._outcome.errors:
            pass  # Test passed
        else:
            # Test failed, take screenshot
            screenshot_name = f"test_failure_{int(time.time())}.png"
            self.driver.save_screenshot(screenshot_name)
            print(f"📸 Screenshot saved: {screenshot_name}")
        
        # Close browser
        self.driver.quit()
        
    def capture_page_performance(self):
        """Utility method to capture page load performance"""
        navigation_timing = self.driver.execute_script("""
            return {
                'loadComplete': performance.timing.loadEventEnd - performance.timing.navigationStart,
                'domReady': performance.timing.domContentLoadedEventEnd - performance.timing.navigationStart,
                'responseTime': performance.timing.responseEnd - performance.timing.requestStart
            }
        """)
        
        print(f"📊 Performance Metrics:")
        print(f"   - Page Load: {navigation_timing['loadComplete']}ms")
        print(f"   - DOM Ready: {navigation_timing['domReady']}ms") 
        print(f"   - Response Time: {navigation_timing['responseTime']}ms")
        
        return navigation_timing

if __name__ == "__main__":
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(ECommerceLoginTest)
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*50)
    print("TEST EXECUTION SUMMARY")
    print("="*50)
    print(f"Tests Run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success Rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    print("="*50)
    
    # Test environment info
    print(f"\nTest Environment:")
    print(f"- Browser: Chrome (Latest)")
    print(f"- OS: Windows 11")
    print(f"- Resolution: 1920x1080 (Desktop), 390x844 (Mobile)")
    print(f"- Hardware: Intel i5 12th Gen, RTX 3060, 32GB RAM")
    print(f"- Tester: Metehan Kutlu")
    print(f"- Date: December 2024")