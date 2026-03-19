from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def open_invu_ge_and_click_login():
    """
    Opens the invu.ge website and clicks on the login link
    """
    url = "https://invu.ge"
    driver = None
    
    try:
        # Setup Chrome driver with WebDriver Manager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        
        print(f"Opening {url}...")
        driver.get(url)
        
        # Wait for the page to load
        time.sleep(3)
        
        # Wait for the login link to be present and clickable
        print("Looking for login link with XPath: //a[@href='/login']")
        wait = WebDriverWait(driver, 10)
        login_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))
        )
        
        print("Found login link, clicking...")
        login_link.click()
        
        print("Successfully clicked on the login link!")
        
        # Wait for the page to load after clicking login
        time.sleep(3)
        
        # Now look for the button with class "font-medium transition-colors"
        print("Looking for button with XPath: //button[@class='font-medium transition-colors']")
        button_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='font-medium transition-colors']"))
        )
        
        print("Found button, clicking...")
        button_element.click()
        
        print("Successfully clicked on the button!")
        
        # Wait for the page to load after clicking the button
        time.sleep(3)
        
        # Now look for the firstName input field and enter text
        print("Looking for firstName input field with XPath: //input[@id='firstName']")
        first_name_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='firstName']"))
        )
        
        print("Found firstName input field, entering text...")
        first_name_input.clear()  # Clear any existing text
        first_name_input.send_keys("anastasia77")
        
        print("Successfully entered 'anastasia77' in the firstName field!")
        
        # Now look for the lastName input field and enter text
        print("Looking for lastName input field with XPath: //input[@id='lastName']")
        last_name_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='lastName']"))
        )
        
        print("Found lastName input field, entering text...")
        last_name_input.clear()  # Clear any existing text
        last_name_input.send_keys("anita222")
        
        print("Successfully entered 'anita222' in the lastName field!")
        
        # Now look for the password input field and enter text
        print("Looking for password input field with XPath: //input[@type='password']")
        password_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        
        print("Found password input field, entering text...")
        password_input.clear()  # Clear any existing text
        password_input.send_keys("anaAna77")
        
        print("Successfully entered 'anaAna77' in the password field!")
        
        # Now look for the email input field and enter text
        print("Looking for email input field with XPath: //input[@id='email']")
        email_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
        )
        
        print("Found email input field, entering text...")
        email_input.clear()  # Clear any existing text
        email_input.send_keys("anastasianefaridze77@gmail.com")
        
        print("Successfully entered 'anastasianefaridze77@gmail.com' in the email field!")
        
        # Now look for the confirmPassword input field and enter text
        print("Looking for confirmPassword input field with XPath: //input[@id='confirmPassword']")
        confirm_password_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='confirmPassword']"))
        )
        
        print("Found confirmPassword input field, entering text...")
        confirm_password_input.clear()  # Clear any existing text
        confirm_password_input.send_keys("anaAna77")
        
        print("Successfully entered 'anaAna77' in the confirmPassword field!")
        
        # Wait a bit to see the result
        time.sleep(5)
        
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False
    
    finally:
        if driver:
            print("Closing browser...")
            driver.quit()

if __name__ == "__main__":
    open_invu_ge_and_click_login()