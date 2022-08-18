from selenium import webdriver
#from selenium.webdriver.commom.keys import Keys
#from BeautifulSoup import BeautifulSoup as bs4
from requests import *
import pandas as pd 
from LINKS.links import facebook_url


driver = webdriver.Firefox()

driver.get(facebook_url)

from time import sleep
sleep(10)
username_input = driver.find_element_by_name("email")
username_input.click()
username_input.send_keys('')

sleep(2)

pwd_input = driver.find_element_by_name('pass')
pwd_input.click()
pwd_input.send_keys('')


submit_btn = driver.find_element_by_name("login")
submit_btn.click()

sleep(20)

status_box = driver.find_element_by_class_name("jcxyg2ei alzwoclg")
status_box.click()
status_box.send_keys('status postado pelo selenium')

sleep(2)


post_status_btn = driver.find_element_by_class_name("""gvxzyvdx aeinzg81 t7p7dqev
                                               gh25dzvf exr7barw b6ax4al1
                                               gem102v4 ncib64c9 mrvwc6qr
                                               sx8pxkcf f597kf1v cpcgwwas
                                               m2nijcs8 hxfwr5lz k1z55t6l
                                               oog5qr5w innypi6y qtx5e3l4""")

post_status_btn.click()
