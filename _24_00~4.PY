import os
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

LINKEDIN_LOGIN_URL = os.environ.get('LINKEDIN_LOGIN_URL', 'LINKEDIN_LOGIN_URL not set')
FILTER_SEARCH_URL = os.environ.get('FILTER_SEARCH_URL', 'FILTER_SEARCH_URL not set')
FIRST_NAME = os.environ.get('FIRST_NAME', 'FIRST_NAME not set')
LAST_NAME = os.environ.get('LAST_NAME', 'LAST_NAME not set')
EMAIL = os.environ.get('EMAIL', 'EMAIL not set')
LINKEDIN_PASSWORD = os.environ.get('LINKEDIN_PASSWORD', 'LINKEDIN_PASSWORD not set')
PHONE_NUMBER = os.environ.get('PHONE_NUMBER', 'PHONE_NUMBER not set')
COLLEGE_OR_UNIVERSITY_ATTENDED = os.environ.get('COLLEGE_OR_UNIVERSITY_ATTENDED', 'COLLEGE_OR_UNIVERSITY_ATTENDED not set')
DEGREE = os.environ.get('DEGREE', 'DEGREE not set')
LINKED_IN_PROFILE_URL = os.environ.get('LINKED_IN_PROFILE_URL', 'LINKED_IN_PROFILE_URL not set')
GIT_OR_GITHUB_REPO = os.environ.get('GIT_OR_GITHUB_REPO', 'GIT_OR_GITHUB_REPO not set')


def setup_chrome_driver_for_selenium():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(LINKEDIN_LOGIN_URL)
    return driver

driver = setup_chrome_driver_for_selenium()

driver.get(FILTER_SEARCH_URL)

def maximize_a_window():
    try:
        driver.maximize_window()
    except Exception as e:
        print(f"initial maximize window failed. adjusting the window a different way: {e}")
        driver.set_window_size(1920, 1080)  # full hd resolution size

time.sleep(0)

Email_or_phone_id = driver.find_element(By.ID, "username")
Email_or_phone_id.send_keys(EMAIL)

Password_id = driver.find_element(By.ID, "password")
Password_id.send_keys(LINKEDIN_PASSWORD + Keys.ENTER)

try:
    page_loaded_indicator = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//some_xpath_indicating_page_has_loaded"))
    )
except TimeoutException:
    print("the job search page did not load within 30 seconds.")

try:
    easy_apply_first_click = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "span.artdeco-button__text"))
    )
    easy_apply_first_click.click()
except TimeoutException:
    print("the first easy apply button was not clickable within 30 seconds.")