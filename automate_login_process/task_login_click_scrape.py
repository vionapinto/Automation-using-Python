from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

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
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()

    # find and fill username and password
    driver.find_element(by="id", value="id_username").send_keys("automated")
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    
    # wait 2 seconds and hit home key
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    print(driver.current_url)

    time.sleep(2)  # if you dont wait for some time here, it will say out of range, since it has no temp value yet
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    text = str(clean_text(element.text))
    return text

print(main())

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from datetime import datetime as dt

# service = Service('/home/dci-student/Downloads/chromedriver.exe')

# def get_drvier():
#   # Set options to make browsing easier
#   options = webdriver.ChromeOptions()
#   options.add_argument("disable-infobars")
#   options.add_argument("start-maximized")
#   options.add_argument("disable-dev-shm-usage")
#   options.add_argument("no-sandbox")
#   options.add_experimental_option("excludeSwitches", ["enable-automation"])
#   options.add_argument("disable-blink-features=AutomationControlled")

#   driver = webdriver.Chrome(service=service, options=options)
#   driver.get("http://automated.pythonanywhere.com")
#   return driver

# def clean_text(text):
#   """Extract only the temperature from text"""
#   output = float(text.split(": ")[1])
#   return output

# def write_file(text):
#   """Write input text into a text file"""
#   filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
#   with open(filename, 'w') as file:
#     file.write(text)


# def main():
#   driver = get_drvier()
#   while True:
#     time.sleep(2)
#     element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
#     text = str(clean_text(element.text))
#     write_file(text)
    
# print(main())