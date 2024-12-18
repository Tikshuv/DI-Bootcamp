# Task
# Initialize Selenium WebDriver
# Navigate to the Web Page : scrapethissite
# Since the page contains frames, identify each frame and switch to it to access its content.
# Use Selenium to navigate through frames and extract necessary data.
# After switching to a frame, use BeautifulSoup to parse and extract data.
# Focus on extracting specific information like text, links, or any other relevant content from each frame.
# Structure the extracted data into a structured format like a list of dictionaries or a pandas DataFrame.
# Save the data to a CSV file for further analysis or use.
# Properly close the Selenium WebDriver session.
#
#
# Expected Deliverables
# A Python script that successfully navigates the frames and scrapes data from the “Scrape This Site” Frames page.
# A CSV file or similar containing the structured data you extracted.
import requests
import time
import pandas as pd
import json
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

url = "https://www.scrapethissite.com/pages/frames/"
driver.get(url)
wait = WebDriverWait(driver, 10)

iframe = driver.find_element(By.ID, 'iframe')
driver.switch_to.frame(iframe)
turtles_len = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'btn-default')))
t = 0
# print(len(turtles_len))
tortoises = []
for t in range(len(turtles_len)):
    turtles_b = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn-default")))
    # print(len(turtles_b))
    turtles_b[t].click()
    # time.sleep(1) changed waiting instead of image to description as it's easier to make unique key and flag
    description = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "lead")))
    # img = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "turtle-image")))
    img = driver.find_element(By.CLASS_NAME, "turtle-image")
    name = driver.find_element(By.CLASS_NAME, 'family-name')
    file_name = f"{name}.jpg"
    response = requests.get(img.get_attribute("src"))
    with open(file_name, "wb") as f:
        f.write(response.content)
    # print(name.text)
    # description = driver.find_element(By.CLASS_NAME, 'lead')
    turtle = {'Name': name.text, 'Description': description.text, 'image': img.get_attribute('src')}
    tortoises.append(turtle)
    # print('turtle')
    turtle_b = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-default")))
    turtle_b.click()
    time.sleep(1)

df = pd.DataFrame(tortoises)
csv_file = "turtle_data.csv"
df.to_csv(csv_file, index=False)
print(f"Data saved to {csv_file}")

with open('tortoises.json', 'w') as json_file:
    json.dump(tortoises, json_file)

# that was way easier than ex_1....