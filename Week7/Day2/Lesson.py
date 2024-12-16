from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pprint  # To tidy up

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
driver = webdriver.Chrome(options=options)
url = "https://blog.hubspot.com/website/website-pop-up-examples"
driver.get(url)
wait = WebDriverWait(driver, 10)
try:
    cookie_close_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-labelledby="hs-eu-cookie-close-button"]'))
    )
    cookie_close_button.click()
    print("Cookie close button clicked.")
    mail_close_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="blog-exit-intent-header-close cl-close"]'))
    )
    mail_close_button.click()
    print("Mail close button clicked.")

except Exception as e:
    print(f"An error occurred: {e}")

driver.quit()