import logging
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium import webdriver
import openpyxl

from Var import excel_file, capabilities_sheet, server, samsung_dialpad_locator, \
    phone_type, key_locator, samsung_dial_button_locator, dial_button_locator,ph_number_locator \
    google_dialpad_locator,main_activity,main_package

# Funtion Opens the dialer app on the device under test

def open_dialer(device):
    if device == '1':
        desired_caps = get_caps(excel_file, capabilities_sheet, 1)
        driver = webdriver.Remote(server, desired_caps)
        driver.implicitly_wait(2)
        driver.find_element(By.ID, value=samsung_dialpad_locator).click()
    elif device == '2':
        desired_caps = get_caps(excel_file, capabilities_sheet, 2)
        driver = webdriver.Remote(server, desired_caps)
        driver.implicitly_wait(2)
        driver.find_element(By.ID, value=google_dialpad_locator).click()
    elif device == '3':
        pass
    else:
        pass
    return driver  
      
# Function to return the driver for the intended device      
def get_driver(device):
    if device == '1':
        desired_caps = get_caps(excel_file, capabilities_sheet, 1)
        desired_caps['appActivity'] = ''
        desired_caps['appPackage'] = ''
        driver = webdriver.Remote(server, desired_caps)
        
    elif device == '2':
        desired_caps = get_caps(excel_file, capabilities_sheet, 2)
        desired_caps['appActivity'] = ''
        desired_caps['appPackage'] = ''
        driver = webdriver.Remote(server, desired_caps)
    elif device=='3':
        pass
    else:
        pass
            
    return driver
  
# This program dials a number by pasting the number on the keypad edit text field using send_key function

def dial_a_number_by_copypaste(driver, number):
    dl=driver.find_element(by=AppiumBy.XPATH, value=ph_number_locator).send_keys(number)
    driver.find_element(by=AppiumBy.ID, value=dial_button_locator).click()

#  This program dials a number using the native dialer keypad.

def dial_a_number(driver, number):
    for num in str(number):
        if num == '1':
            # print('1')
            driver.find_element(By.ID, value=mylocator + "one").click()
        elif num == '2':
            # print('2')
            driver.find_element(By.ID, value=mylocator + "two").click()
        elif num == '3':
            # print('3')
            driver.find_element(By.ID, value=mylocator + "three").click()
        elif num == '4':
            # print('4')
            driver.find_element(By.ID, value=mylocator + "four").click()
        elif num == '5':
            # print('5')
            driver.find_element(By.ID, value=mylocator + "five").click()
        elif num == '6':
            # print('6')
            driver.find_element(By.ID, value=mylocator + "six").click()
        elif num == '7':
            # print('7')
            driver.find_element(By.ID, value=mylocator + "seven").click()
        elif num == '8':
            # print('8')
            driver.find_element(By.ID, value=mylocator + "eight").click()
        elif num == '9':
            # print('9')
            driver.find_element(By.ID, value=mylocator + "nine").click()
        elif num == '0':
            # print('0')
            driver.find_element(By.ID, value=mylocator + "zero").click()
        elif num == '*':
            # print('*')
            driver.find_element(By.ID, value=mylocator + "star").click()
        elif num == '#':
            # print('#')
            driver.find_element(By.ID, value=mylocator + "pound").click()
  

    driver.find_element(By.ID, value=dial_button).click()

#   This function accepts the call and verifies if it is connected

def accept_call(device):
    desired_caps = get_caps(excel_file, capabilities_sheet, device)

    desired_caps['appActivity'] = main_activity
    desired_caps['appPackage'] = main_package
    driver = webdriver.Remote(server, desired_caps)
    driver.open_notifications()
    driver.implicitly_wait(5)
    if device == '1':  # new
        driver.find_element_by_accessibility_id('Accept').click()
        driver.implicitly_wait(2)
        dl = driver.find_element(by=AppiumBy.XPATH,
                                 value=mute_button_loactor_1)
    elif device == '2':
        driver.find_element_by_accessibility_id('Answer').click()
        driver.implicitly_wait(2)
        dl = driver.find_element(by=AppiumBy.XPATH,
                                 value=mute_button_locator_2)
    elif device=='3':
        pass
    else:
        pass

    verify_connection = dl.is_enabled()
    if verify_connection is True:
        logging.info('Call is Connected')
    else:
        logging.info('Call is not connected')

    return driver

#   This function ends the call

def end_call(device):
    desired_caps = get_caps(excel_file, capabilities_sheet, device)
    desired_caps['appActivity'] = 'com.sec.android.app.launcher.activities.LauncherActivity'
    desired_caps['appPackage'] = 'com.sec.android.app.launcher'
    driver = webdriver.Remote(server, desired_caps)
    driver.open_notifications()
    driver.implicitly_wait(2)
    if device == '1':
        driver.find_element_by_accessibility_id('End call').click()
    elif device == '2':
        driver.find_element_by_accessibility_id('Decline').click()
    elif device == '3':
        pass
    else:
        pass
      
      
