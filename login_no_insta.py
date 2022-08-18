from selenium import webdriver
#from selenium.webdriver.commom.keys import Keys
#from BeautifulSoup import BeautifulSoup as bs4
from requests import *
import pandas as pd 
from LINKS.links import insta_url


driver = webdriver.Firefox()

driver.get(insta_url)

from time import sleep
sleep(10)
username_input = driver.find_element_by_name("username")
username_input.click()
username_input.send_keys('juniomiguelsizeg@gmail.com')

sleep(2)

pwd_input = driver.find_element_by_name('password')
pwd_input.click()
pwd_input.send_keys('mj104598')


submit_btn = driver.find_elements_by_class_name("qF0y9Igw0EIwRSHeGOV_acqo5_4EzTm")
submit_btn.click()


