from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

BASE_URL = "https://invu.ge"
EMAIL = os.getenv("INVU_EMAIL", "your_email@example.com")
PASSWORD = os.getenv("INVU_PASSWORD", "your_password")


def create_driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def login_test():
    driver = create_driver()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get(BASE_URL)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.secondary-button"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys(EMAIL)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))).send_keys(PASSWORD)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    finally:
        driver.quit()


if __name__ == "__main__":
    login_test()
