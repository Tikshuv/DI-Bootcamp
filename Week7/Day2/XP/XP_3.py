import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Configure Selenium (replace with your webdriver path)
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

# URL of the BBC Weather page
url = "https://www.bbc.com/weather/3435910"
driver.get(url)

# Wait for the page to load (adjust timeout as needed)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".wr-day"))
    )
except Exception as e:
    print(f"Error waiting for page elements: {e}")
    driver.quit()
    exit()

# Get the page source after dynamic content loading
page_source = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Extract data (customize based on the actual webpage structure)
dates = []
temperatures = []
descriptions = []


daily_info = soup.find_all("div", class_="wr-day")
for day in daily_info:
    date_element = day.find("span", class_="wr-day__date")
    temp_element = day.find("span", class_="wr-value--temperature--c")
    desc_element = day.find("span", class_="wr-day__weather-type-description")

    if date_element:
        dates.append(date_element.text.strip())
    else:
        dates.append("N/A")

    if temp_element:
        temperatures.append(int(temp_element.text.strip().split()[0]))
    else:
        temperatures.append(None)

    if desc_element:
      descriptions.append(desc_element.text.strip())
    else:
      descriptions.append("N/A")


driver.quit()


# Create a Pandas DataFrame
weather_data = pd.DataFrame({"Date": dates, "Temperature (°C)": temperatures, "Description":descriptions})

# Basic data cleaning (handle missing values)
weather_data["Temperature (°C)"].fillna(weather_data["Temperature (°C)"].mean(), inplace=True)
weather_data["Temperature (°C)"] = weather_data["Temperature (°C)"].astype(int)

# Data analysis and visualization

print(weather_data)
print(weather_data.describe())

# Line plot of temperature over time
plt.figure(figsize=(10, 6))
sns.lineplot(x="Date", y="Temperature (°C)", data=weather_data)
plt.title("Tel Aviv Temperature Forecast")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar chart of daily descriptions
plt.figure(figsize=(10, 6))
sns.countplot(x="Description", data=weather_data)
plt.title("Tel Aviv Weather Description Frequency")
plt.xlabel("Description")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()