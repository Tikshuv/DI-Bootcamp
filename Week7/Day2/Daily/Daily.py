# prompt: Daily Challenge: Web Scraping and Data Visualization
# Your Task
# Instructions
# Use this webpage : Tel Aviv - BBC Weather
# Scrape the Webpage: Use Python libraries like Selenium to interact with the webpage and BeautifulSoup to parse the HTML, Extract relevant data such as dates, numerical values, categories, etc., Organize the scraped data into a structured format.
# Data Analysis with Pandas:
# Load your scraped data into a Pandas DataFrame.
# Clean and preprocess the data if necessary (handling missing values, type conversion, etc.).
# Perform basic analysis, such as calculating averages, totals, or trends over time.
# Data Visualization with Seaborn and Matplotlib:
# Use Seaborn and Matplotlib to create visualizations that provide insights into the data.
# Examples of visualizations can include line plots for trends over time, bar charts for comparing categories, or heatmaps for showing data density.
# Ensure your visualizations are well-labeled with clear titles, axis labels, and legends where appropriate.
# Document Your Findings:
# Create a report summarizing your methodology, analysis, and insights from the visualizations.
# Explain any interesting patterns or insights derived from your data.
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint  # To tidy up
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
driver = webdriver.Chrome(options=options)

url = "https://www.bbc.com/weather/293397"
driver.get(url)

wait = WebDriverWait(driver, 10)
time.sleep(5)
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")


# Find the relevant data elements (This will depend on the webpage's structure. Inspect the page source to find correct elements)
# Example for extracting daily forecast data:
daily_forecasts = []

# Example of extracting data - adapt selectors to actual webpage structure.
soup = BeautifulSoup(driver.page_source, "html.parser")
pattern = re.compile(r'^daylink-(1[0-3]|[1-9])$')
days = soup.find_all(id=pattern)
print(len(days))
for day in days:
  date = day.find("span", class_="wr-date__longish__dotm").text # Replace with the correct class name or other selector
  temps_c = day.find_all("span", class_="wr-value--temperature--c")
  temps = [int(temp.text.replace("°", "")) for temp in temps_c]
  high_temp = temps[0]
  low_temp = temps[1]
  summary = day.find("div", class_="wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque").text # Replace with the correct class name or other selector
  daily_forecasts.append([date, high_temp, low_temp, summary])
  print(date)
  print(high_temp)
  print(low_temp)
  print(summary)

df = pd.DataFrame(daily_forecasts, columns=["Date", "High Temp", "Low Temp", "Summary"])
driver.quit()
df["High Temp"] = pd.to_numeric(df["High Temp"], errors='coerce')
df["Low Temp"] = pd.to_numeric(df["Low Temp"], errors='coerce')
plt.figure(figsize=(10, 6))
sns.lineplot(x="Date", y="High Temp", data=df, marker='o')
plt.title("Daily High Temperatures in Tel Aviv")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
average_high_temp = df["High Temp"].mean()
print(f"Average high temperature: {average_high_temp:.2f} °C")