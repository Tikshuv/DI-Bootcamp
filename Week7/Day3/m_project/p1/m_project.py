# Task
# Initialize Selenium WebDriver
# Load the Web Page
# Identify the elements that contain hosting plan details.
# Extract necessary data such as plan names, features, and pricing.
# Store and Save the Data
# Close Selenium WebDriver

import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint  # To tidy up

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
driver = webdriver.Chrome(options=options)

url = "https://www.inmotionhosting.com/"
driver.get(url)

wait = WebDriverWait(driver, 10)
# time.sleep(1)
shared_h = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="home-rostrum-3"]/div/div/div[1]/div[2]/div[2]/a')))
shared_h.click()
# ok I learned that I can copy XPATH instead of trying to figure out what it is, especially when there're issues with...
# #
# time.sleep(4)
# compare_button = driver.find_element("link text", "Compare Plans")
# compare_button.click()
# time.sleep(4)
# plan_cards = driver.find_elements(By.CLASS_NAME, "imh-rostrum-card")
#
# # List to store extracted data
# plans_data = []
#
# # Iterate through each card
# for card in plan_cards:
#     # Extract name
#     name = card.find_element(By.CLASS_NAME, "imh-rostrum-card-title").text
#     description = card.find_element(By.CLASS_NAME, "imh-rostrum-sub-title").text
#
#     starting_price_element = card.find_element(By.XPATH, ".//*[starts-with(text(), '$')]")
#     starting_price = starting_price_element.text
#
#     renewal_price = card.find_element(By.XPATH,".//div[contains(@class, 'imh-rostrum-starting-at-price-normal')]//span[contains(@class, 'rostrum-price')]").text
#
#     characteristics_elements = card.find_elements(By.CLASS_NAME, "imh-rostrum-detail")
#     characteristics = [char.text for char in characteristics_elements if char.text.strip()]


# switched to BeautifulSoup cause for idk why I fail to extract prices with selenium and getting empty values
soup = BeautifulSoup(driver.page_source, 'html.parser')
plans_data = []
plan_cards = soup.find_all('div', class_='imh-rostrum-card')
for card in plan_cards:
    name = card.find(class_='imh-rostrum-card-title').text
    description = card.find(class_='imh-rostrum-sub-title').text

    prices = card.find_all(class_='rostrum-price')
    starting_price = prices[0].text
    renewal_price = prices[1].text

    characteristics_elements = card.find_all(class_='imh-rostrum-detail')
    # for element in characteristics_elements:
    #     if
    characteristics = [char.text for char in characteristics_elements if char.text.strip()]

    plan_info = {
        "name": name,
        "description": description,
        "starting_price": starting_price,
        "renewal_price": renewal_price,
        "characteristics": characteristics
    }

    plans_data.append(plan_info)

# for plan in plans_data:
#     print(plan)
# print(plans_data[1])
print(plans_data[-1])
# Ill try to fix it later, the structure of this segment just doesn't seem fit for scrapping with how they separated even one text into different
# segments or the opposite one text reappears multiple times. . .

# I'm starting to see tendency that some sites just aren't made for scrapping or the problem is with me