#  Exercise 5 : Scrape and Analyze Weather Data from a JavaScript-Enabled Weather Website
# Task:
# Visit this website.
# Scrape weather forecast data including temperature, condition, and humidity.
# Analyze the data to find the average temperature and most common weather condition.
# Instructions:
# Use Selenium to navigate to the weather forecast page of a specific city.
# Extract and parse the HTML content, focusing on dynamically loaded weather data.
# Using BeautifulSoup, extract relevant weather information like temperature, condition (sunny, cloudy, etc.), and humidity.
# Calculate the average temperature and identify the most common weather condition.
# Print the analysis results.
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint  # To tidy up

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
driver = webdriver.Chrome(options=options)

url = "https://www.accuweather.com/en/us/attica/30607/weather-forecast/2139413"
driver.get(url)

wait = WebDriverWait(driver, 10)

search = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-input")))
search.send_keys("Minsk")
search.send_keys(Keys.RETURN)
time.sleep(7)
minsk = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/web-api/three-day-redirect?key=GEO_27%2E567%2c53%2E900&city=Minsk&postalCode=&target=')]")))
minsk.click()
time.sleep(7)
soup = BeautifulSoup(driver.page_source, "html.parser")
days = soup.find_all(class_='daily-list-item ')
temps = soup.find_all(class_='temp-hi')
temps_int = [int(temp.text.replace("°", "")) for temp in temps]
avg_temps = sum(temps_int) / len(temps_int)
print('Average Temperature:', avg_temps)
conds = ['Wind', 'Rain', 'Sun', 'Cloud']
get_conds = soup.find_all(class_='no-wrap')
main_conds = []
for i, cond in enumerate(conds):
    if i%2 == 1:
        main_conds.append(cond)
condition_counts = {condition: 0 for condition in conds}
for item in main_conds:
    for condition in conds:
        if condition.lower() in item.lower():
            condition_counts[condition] += 1
print(condition_counts)