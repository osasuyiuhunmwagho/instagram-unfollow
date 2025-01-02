
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains 
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import StaleElementReferenceException
# import time
  
# username = "suyisarchives_"
# password = "maynosa561"
# def login(driver):
       
#         driver.find_element(By.NAME,"username").send_keys(username)
#         driver.find_element(By.NAME,"password").send_keys(password)
        
#         #there are "." in between the "_" thats why it difnt work
#         driver.find_element(By.CSS_SELECTOR,"._acan._acap._acas._aj1-._ap30").click()
# def click_button_css(driver, css_selector):
#                 try:
#                         print(f"Clicking button with CSS selector: {css_selector}")
#                         element = WebDriverWait(driver, 20).until(
#                                 EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
#                         element.click()
#                 except StaleElementReferenceException:
#                         print("Encountered a stale element, trying again...")
#                         element = WebDriverWait(driver, 20).until(
#                                  EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
#                                 )
#                         element.click()
           
        
        
# def navigate_to_followers(driver):
#        dropdown_css =  '[alt*="'+ username +  '"] '
#        profile_css = "[href*=\""+ username +  "\"]"
#        click_button_css(driver, dropdown_css)
#        click_button_css(driver, profile_css)

# def no_follow_back(followers,following):
#         followers.sort()
#         following.sort()
#         no_followback_list = []
#         for i in range(len(following)):
#                 try:
#                         no_followers = followers.index(following[i])
#                 except ValueError:
#                         no_followback_list += no_followers
#         return no_followback_list           

        
# def main():
       
      
#         # Initialize the Chrome driver correctly with WebDriver Manager
#         #chroem wasnt opening so i used the 'service' object
#         # it is used to seperate driver management from web manipulation. 
#         driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()))
#         driver.get('https://www.instagram.com/')
        
#         #selenium for later versions uses the By class to make it more efficient
#         #use inspect to find the elements name
#         #send_keys is used to type in the username to the textbox
  
#         time.sleep(1)  # Give enough time for the page to load
#         # Always a good practice to close the driver after completion
#         login(driver)
       
#         navigate_to_followers(driver)
        
        
#         time.sleep(3)

#         followers_css = "[href*=\"" + username + "/followers/\"]"
#         css_close_buttton = "[aria-label='Close']"
#         following_css = "[href*=\""+ username + "/following/\"]"

#         click_button_css(driver, followers_css)
#         followers_list = get_usernames_from_dialog(driver)
       
#         time.sleep(2)

#         click_button_css(driver, css_close_buttton)
#         time.sleep(7)
        
#         following_list = get_usernames_from_dialog(driver)
#         click_button_css(driver, following_css)
      
#         time.sleep(10)
#         return

# def get_usernames_from_dialog(driver):
#         print("problem here")
#         list_xpath = '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div'
#         print("problem here")

#         #waiting till everything in the dialog is located
#         print("problem here")
        
#         WebDriverWait(driver, 20).until(
#                EC.presence_of_element_located((By.XPATH, list_xpath)))

#         #ActionChains(driver).send_keys(Keys.END).perform()
#         scroll_down(driver)
#         time.sleep(3)
#         #stores the list of all the elements
#         list_elements = driver.find_elements(By.CSS_SELECTOR, "a[href*='/']")
#         time.sleep(5)

#         followers = []     

#         for element in list_elements:
#                 href = element.get_attribute('href')  # Get the href attribute
#                 if href:  # Check if href exists
#                         followers.append(href.split("/")[3])  # Extract and append part of the URL
#                 else:
#                         continue
# def scroll_down(driver):
        

#         # Get scroll height
#         last_height = driver.execute_script("return document.body.scrollHeight")

#         while True:
#         # Scroll down to bottom
#                 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#                 # Wait to load page
#                 time.sleep(2)

#                 # Calculate new scroll height and compare with last scroll height
#                 new_height = driver.execute_script("return document.body.scrollHeight")
#                 if new_height == last_height:
#                         break
#                 last_height = new_height
                                         
    
# main()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time
from webdriver_manager.chrome import ChromeDriverManager


username = "suyisarchives_"
password = "maynosa561"


def login(driver):
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    
    # Click login button (modify the selector if necessary)
    driver.find_element(By.CSS_SELECTOR, "._acan._acap._acas._aj1-._ap30").click()


def click_button_css(driver, css_selector):
    try:
        print(f"Clicking button with CSS selector: {css_selector}")
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    except (StaleElementReferenceException, TimeoutException):
        print("Encountered a stale element, trying again...")
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        element.click()


def navigate_to_followers(driver):
    dropdown_css = '[alt*="' + username + '"] '
    profile_css = "[href*=\"" + username + "\"]"
    click_button_css(driver, dropdown_css)
    click_button_css(driver, profile_css)


def no_follow_back(followers, following):
      return [
        user for user in following 
        if user not in set(followers)
    ]


def main():
    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()))
    driver.get('https://www.instagram.com/')

    time.sleep(1)
    login(driver)
   
    navigate_to_followers(driver)
    
    time.sleep(3)

    followers_css = "[href*=\"" + username + "/followers/\"]"
    css_close_button = "[aria-label='Close']"
    following_css = "[href*=\"" + username + "/following/\"]"

    # Click to open followers dialog
    click_button_css(driver, followers_css)
    followers_list = get_usernames_from_dialog(driver)
   
    time.sleep(2)

    # Close the followers dialog
    click_button_css(driver, css_close_button)
    time.sleep(3)
    
    # Click to open following dialog
    click_button_css(driver, following_css)
    following_list = get_usernames_from_dialog(driver)
    print(followers_list)
    
    # Compare followers and following, and get the list of users not following back
    no_followback_list = no_follow_back(followers_list, following_list)
    
    # Print or return the result
    print("Users not following back:", no_followback_list)
    time.sleep(10)



def get_usernames_from_dialog(driver):
    time.sleep(5)
    modal = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//ul"))
    )
    scroll_down_page(driver,modal)
    
 

def scroll_down_page(driver, modal):
    last_height = driver.execute_script("return arguments[0].scrollHeight", modal)

    while True:
        # Scroll down the modal
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(2)
        print("scrolling")
        new_height = driver.execute_script("return arguments[0].scrollHeight", modal)
        if new_height == last_height:
            break
        last_height = new_height


main()