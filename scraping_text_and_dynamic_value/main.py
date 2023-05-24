#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service('/home/dci-student/Downloads/chromedriver.exe') # absolute path pointing to the chromedriver file

def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage") # to avoid issues particularly with Linux
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(service=service, options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

# Only for the temperature part
def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output

def main():
  driver = get_driver()
  # Aristotle
  #element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]") # we got this by inspecting the website and checking the x path
  #return element.text
  
  #Temperature
  # import time so that you can catch the temperature since it keeps changing
  # you need to stop the scrape for two seconds so that you can catch the temp
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)

print(main())