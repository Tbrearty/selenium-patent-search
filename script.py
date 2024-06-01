# script.py

# Install necessary libraries and Chrome
!pip install selenium
!pip install webdriver-manager
!apt-get update
!apt-get install -y wget unzip
!wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
!sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
!apt-get update
!apt-get install -y google-chrome-stable

# Set up and run Selenium script
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Add the current working directory to the system path
os.environ["PATH"] += os.pathsep + os.getcwd()

# Download ChromeDriver
chrome_driver_version = '114.0.5735.90'
!wget -N https://chromedriver.storage.googleapis.com/{chrome_driver_version}/chromedriver_linux64.zip
!unzip -o chromedriver_linux64.zip
!chmod +x chromedriver
!mv -f chromedriver /usr/local/bin/chromedriver

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = '/usr/bin/google-chrome-stable'

# Specify the path to the ChromeDriver binary
chrome_driver_path = '/usr/local/bin/chromedriver'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Define the search query
search_query = "AI-driven music composition OR real-time soundtrack generation OR customizable user interface OR integration with multimedia projects"
search_url = f"https://patents.google.com/?q={search_query.replace(' ', '+')}"

# Open the search URL
driver.get(search_url)

# Wait for the page to load
time.sleep(5)  # Wait for 5 seconds to ensure the page is fully loaded

# Extract titles
titles = driver.find_elements(By.CSS_SELECTOR, 'a[class="result-title"]')
for title in titles:
    print(title.text)

# Close the driver
driver.quit()
