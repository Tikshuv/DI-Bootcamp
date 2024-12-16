# Exercise 4 : Scrape and Categorize News Articles from a JavaScript-Enabled News Site
# Task:
# Visit this website.
# Scrape news article titles and their publication dates.
# Categorize articles based on their publication month.
# Instructions:
# Use Selenium to navigate to a specific news section on the website.
# Extract and parse the HTML content that is dynamically loaded via JavaScript.
# Using BeautifulSoup, extract news article titles and publication dates.
# Categorize articles by their publication month (e.g., ‘January’, ‘February’, etc.).
# Print the categorized lists of articles.

import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from dateutil.parser import parse
from collections import defaultdict

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
driver = webdriver.Chrome(options=options)

url = "https://www.bbc.com/innovation/technology"
driver.get(url)

wait = WebDriverWait(driver, 10)
news = []
today = datetime.now()
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="2"]')))
button.click()
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="1"]')))
button.click()

while True:
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find_all(class_='sc-76a64d5e-4 lncuML')
    print('New table len:', len(table))
    for new in table:
        date = new.find(attrs={'data-testid':"card-metadata-lastupdated"}).text.strip()
        try:
            date_obj = datetime.strptime(date, '%d %b %Y')
            month_name = date_obj.strftime('%B')
        except ValueError:
            parsed_date = parse(date, fuzzy=True)
            new_date = today - (today - parsed_date)
            month_name = new_date.strftime('%B')
        title = new.find(attrs={'data-testid':"card-headline"}).text.strip()
        print(title)
        print(month_name)
        news.append({'Title': title, 'Month': month_name})

    try:
        # Find the "Next Page" button and check if it is disabled
        next_b = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="pagination-next-button"]')))
        if next_b.get_attribute('disabled') is not None:
            break
        next_b.click()
        time.sleep(1)
        # I could use EC.presence_of_all_elements_located I guess but this EX(more specifically this website) damaged me enough
        print('Next page')# Click the next button
    except Exception as e:
        print(f"Error or no next button found: {e}")
        break


grouped_news = defaultdict(list)

for article in news:
    grouped_news[article['Month']].append(article['Title'])

for month, titles in grouped_news.items():
    print(f"{month}:")
    for title in titles:
        print(f"  - {title}")
    print()