from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime as dt

import time
service = Service('/home/dci-student/Downloads/chromedriver.exe')

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output

def write_file(text):
    # write input text into a text file
    filename = f"{dt.now().strftime('%Y%m%d:%H%M%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)

def main():
    driver = get_driver()

    while True:
        time.sleep(2)
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        text = str(clean_text(element.text))
        write_file(text)

print(main())
