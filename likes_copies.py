from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime


usernameStr = 'copies_store_india'
passwordStr = 'hahahahahe'

browser = webdriver.Chrome()
browser.get(('http://ighoot.com/'))
login_button = browser.find_element_by_id('slogin')
login_button.click()

username_field = browser.find_element_by_name("username")
password_field = browser.find_element_by_name("password")
submit_login_button = browser.find_element_by_xpath("//*[@class='btn btn-primary pull-right']")

username_field.send_keys(usernameStr)
password_field.send_keys(passwordStr)
submit_login_button.click()

browser.implicitly_wait(30)

like = "like?type=photo"
follow_button = browser.find_element_by_xpath('//a[@href="'+like+'"]');
follow_button.click()

wait = WebDriverWait(browser, 30)
wait.until(EC.element_to_be_clickable((By.ID, 'get_likes_button')))

get_like_buttons_list = browser.find_elements_by_id('get_likes_button')
now =  datetime.datetime.now()
index = int(now.hour%3)
get_like_buttons_list[index].click()

logout = "logout"
logout_button = browser.find_element_by_xpath('//a[@href="'+logout+'"]');
logout_button.click()

