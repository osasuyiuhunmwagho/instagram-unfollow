from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time
from webdriver_manager.chrome import ChromeDriverManager


username = "suyisarchives_"
password = "Maynosa2005."


def login(driver):
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    
    # Click login button (modify the selector if necessary!!!)
    driver.find_element(By.CSS_SELECTOR, "._acan._acap._acas._aj1-._ap30").click()


def click_button_css(driver, css_selector):
    try:
        print(f"Clicking button with CSS selector: {css_selector}")
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        
        element.click()

    except (StaleElementReferenceException, TimeoutException):
        print("Encountered a stale element, trying again...")
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        element.click()


def navigate_to_followers(driver):
    #the "* is if the username is in the alt atribute of the image"
    dropdown_css = '[alt*="' + username + '"] '
    #the [href*="username"] is to find the link that contains the username
    #The backslash (\) escapes the double quotes
    inbox_css = "[href*=\"" + "/direct/inbox"+"\""+"]"
    click_button_css(driver, dropdown_css)
    click_button_css(driver, inbox_css)



def main():
    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()))
    driver.get('https://www.instagram.com/')

    time.sleep(1)
    login(driver)
   
    navigate_to_followers(driver)

  
    time.sleep(10)

main()
