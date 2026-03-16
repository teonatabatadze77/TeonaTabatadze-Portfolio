from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
options = Options()
options.add_argument("--start-maximized")

# Set up the Chrome driver (make sure chromedriver is installed and in PATH)
service = Service()  # You can specify the path to chromedriver if needed
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the website
    driver.get("https://invu.ge")
    time.sleep(2)  # Wait for the page to load

    # Click the element with class 'secondary-button'
    secondary_button = driver.find_element(By.CSS_SELECTOR, "a[class='secondary-button']")
    secondary_button.click()
    time.sleep(2)  # Wait for the page to load
    
    # Fill in the email field
    email_field = driver.find_element(By.XPATH, "//input[@type='email']")
    email_field.send_keys("gagoshidzetam55@gmail.com")
    
    # Fill in the password field
    password_field = driver.find_element(By.XPATH, "//input[@type='password']")
    password_field.send_keys("tamarAR77")
    
    # Click the submit button
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    time.sleep(3)  # Wait for login to complete
    
    # Click on the second anchor element in the header
    header_link = driver.find_element(By.CSS_SELECTOR, "header[class='fixed top-0 left-0 right-0 z-50 navbar-container'] a:nth-child(2)")
    header_link.click()
    
    time.sleep(2)  # Wait for page to load
    
    # Click on the same header element again
    header_link_2 = driver.find_element(By.CSS_SELECTOR, "header[class='fixed top-0 left-0 right-0 z-50 navbar-container'] a:nth-child(2)")
    header_link_2.click()
    
    time.sleep(2)  # Wait for page to load
    
    # Click on the Simple Wedding template
    template_element = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Select Simple Wedding template'] div:nth-child(3)")
    template_element.click()
    
    time.sleep(2)  # Wait for template to load
    
    # Click on the gradient button
    gradient_button = driver.find_element(By.CSS_SELECTOR, "button[class='w-full bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 disabled:from-gray-400 disabled:to-gray-500 text-white font-semibold py-3 px-4 rounded-lg transition-all duration-200']")
    gradient_button.click()
    
    time.sleep(2)  # Wait for page to load
    
    # Click on the amber-to-orange gradient button
    amber_button = driver.find_element(By.CSS_SELECTOR, "button[class='w-full bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 disabled:from-gray-400 disabled:to-gray-500 text-white font-bold py-4 px-6 rounded-xl transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105 disabled:hover:scale-100 disabled:cursor-not-allowed']")
    amber_button.click()
    
    time.sleep(2)  # Wait for page to load
    
    # Click on the amber-to-orange gradient button again
    amber_button_2 = driver.find_element(By.CSS_SELECTOR, "button[class='w-full bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 disabled:from-gray-400 disabled:to-gray-500 text-white font-bold py-4 px-6 rounded-xl transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105 disabled:hover:scale-100 disabled:cursor-not-allowed']")
    amber_button_2.click()
    
    time.sleep(2)  # Wait for page to load
    
    # Click on the "Create Invitation" button
    create_invitation_button = driver.find_element(By.XPATH, "//button[normalize-space()='Create Invitation']")
    create_invitation_button.click()
    
    time.sleep(2)  # Wait to see the result
    
    # Click on the amber-to-orange gradient button with specific styling
    gradient_button = driver.find_element(By.XPATH, "//button[@class='w-full bg-gradient-to-r from-amber-500 to-orange-500 text-white py-3 px-4 rounded-lg font-semibold text-sm shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none']")
    gradient_button.click()
    
    time.sleep(2)  # Wait to see the result

finally:
    driver.quit()