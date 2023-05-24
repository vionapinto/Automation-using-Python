from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

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
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def main():
    driver = get_driver()
    # now instead of using x path, while we inspected the website, we see that the username input field has an id, so we will use this.
    driver.find_element(by="id", value="id_username").send_keys("automated") # automated is the username
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN) #automatedautomated is the password
    # keys.RETURN makes it click on the enter button
    # we don't need to assign variable name here or return anything because we are not performing scraping here
    #print(driver.current_url)  # prints out http://automated.pythonanywhere.com/dashboard/ so we know it has clicked enter after typing username and password
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click() # clicking on the HOME button
    print(driver.current_url)

print(main())