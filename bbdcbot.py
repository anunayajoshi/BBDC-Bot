from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import requests
from datetime import datetime as dt
from selenium.webdriver.chrome.options import Options

import subprocess
import os
import time
import getpass


options = Options()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

PATH = "D:\\chromedriver.exe"


path_to_chrome_cookie="user-data-dir=C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\User Data"%(getpass.getuser())

options.add_argument(path_to_chrome_cookie) 

browser = webdriver.Chrome(PATH, options=options)

time.sleep(2)

browser.get("https:/info.bbdc.sg/members-login/")


browser.find_element_by_id('txtNRIC').send_keys("*censored")

time.sleep(2)

browser.find_element_by_id('txtPassword').send_keys("*censored*")

time.sleep(2)

# frames = browser.find_elements_by_tag_name("iframe")
# browser.switch_to.frame(frames[0])
# time.sleep(2)

# browser.find_element_by_class_name("recaptcha-checkbox-border").click()

# time.sleep(3)

# browser.switch_to.default_content()

browser.find_element_by_name('btnLogin').click()

time.sleep(3)

while True: 

    browser.switch_to.frame("leftFrame")


    booking = browser.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[14]/td[3]/a')

    booking.click()

    time.sleep(3)


    browser.switch_to.default_content()

    browser.switch_to.frame('mainFrame')



    month = browser.find_element_by_name('allMonth')

    month.click()


    sessions = browser.find_element_by_name('allSes')

    sessions.click()

    days = browser.find_element_by_name('allDay')

    days.click()

    search = browser.find_element_by_name('btnSearch')

    search.click()

    time.sleep(3)

    # browser.switch_to.alert.accept()

    # time.sleep(5)

    firstDate = browser.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/form/table[1]/tbody/tr[9]/td/table/tbody/tr[3]/td[1]')

    

    
    

    firstSlot = str(firstDate.text)[0:10]

    a = dt.strptime(firstSlot, "%d/%m/%Y")
    b = dt.strptime("22/01/2021", "%d/%m/%Y")

    

    if a >= b:
        print('The time is', dt.now(), '. No slots available. Earliest slot is', firstSlot)

    if a < b:
        lol = 'Slot available on', firstSlot
        print (lol)
        base_url = 'https://api.telegram.org/bot1289510289:AAH5GJb98RwEwW04nPWskQnapET8yIW8WdA/sendMessage?chat_id=-468283052&text="{}"'.format(lol)

        requests.get(base_url)

    time.sleep(120)

    browser.refresh()
