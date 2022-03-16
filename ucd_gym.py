
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 

def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

student_number = input('Enter your student number : ')
student_number2 = input('Enter your student number : ')
input('Press Enter button to run')

#for using chrome
browser=webdriver.Chrome('chromedriver')
browser2=webdriver.Chrome('chromedriver')

browser.get("https://hub.ucd.ie/usis/W_HU_MENU.P_PUBLISH?p_tag=GYMBOOK")
browser2.get("https://hub.ucd.ie/usis/W_HU_MENU.P_PUBLISH?p_tag=GYMBOOK")
browser.implicitly_wait(5)
browser2.implicitly_wait(5)

# checking if there is an available slot
boolean = False
i = 0
while boolean == False:
    try:
        browser.find_element_by_css_selector('#SW300-1\|{0} > td:nth-child(6) > a:nth-child(1)'.format(i)).click()
        browser2.find_element_by_css_selector('#SW300-1\|{0} > td:nth-child(6) > a:nth-child(1)'.format(i)).click()
        break
    except NoSuchElementException:
        i = i + 1
    


browser.implicitly_wait(5)
browser.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click() 

field = browser.find_element_by_xpath('//*[@id="single-column-content"]/div/div/div/div[2]/div/form/input[4]')
field.send_keys(student_number)

proceed_with_booking = browser.find_element_by_xpath('//*[@id="single-column-content"]/div/div/div/div[2]/div/form/input[5]')
proceed_with_booking.click()

confirm = browser.find_element_by_xpath('//*[@id="single-column-content"]/div/div/div/div[2]/div/a[1]')
confirm.click()


### repeat instructions
browser2.implicitly_wait(5)
browser2.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

field2 = browser2.find_element_by_xpath('//*[@id="single-column-content"]/div/div/div/div[2]/div/form/input[4]')
field2.send_keys(student_number2)

proceed_with_booking2 = browser2.find_element_by_xpath('//*[@id="single-column-content"]/div/div/div/div[2]/div/form/input[5]')
proceed_with_booking2.click()

confirm2 = browser2.find_element_by_xpath('//*[@id="single-column-content"]/div/div/div/div[2]/div/a[1]')
confirm2.click()


