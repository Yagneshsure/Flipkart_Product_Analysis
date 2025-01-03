from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/usr/bin/chromium-browser"  # Path to Chromium

# Set logging preferences
options.add_argument("--headless")  # Optional: To run in headless mode
options.add_argument("--disable-gpu")  # Optional: To avoid GPU-related issues
options.add_argument("--no-sandbox")  # Optional: For running in containers or restricted environments

service = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=options)

# Test setup
driver.get("https://www.google.com")
print(driver.title)

driver.quit()
