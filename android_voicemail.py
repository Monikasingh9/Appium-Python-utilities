import time
from appium import webdriver
from configparser import ConfigParser
from appium.webdriver.common.appiumby import AppiumBy
import logging
import os


config = ConfigParser()
config.read("./Resources/config.ini")
server = config.get('Server', 'server_url')
desired_caps = {'platformName': config.get('Desired Capabilities', 'platformName'),
                'automationName': config.get('Desired Capabilities', 'automationName')}


def open_dialer_app(device):
    dial_keypad = ''
    if device == '1':
        desired_caps['udid'] = udid_1
        desired_caps['appPackage'] = dialer_app_1
        desired_caps['appActivity'] = dialer_activity_1
        dial_keypad = dial_pad_locator_1

    elif device == '2':
        desired_caps['udid'] = udid_2
        desired_caps['appPackage'] = dialer_app_2
        desired_caps['appActivity'] = dialer_activity_2
        dial_keypad = dial_pad_locator_2

    elif device == '3':
        pass
    elif device == '4':
        pass
    else:
        pass

    driver = webdriver.Remote(server, desired_caps)
    driver.find_element(AppiumBy.ID, dial_keypad).click()
    return driver


def dial_a_number(device_from, device_to):
    driver = open_dialer_app(device_from)
    ph_num = config.get('Phone Numbers', 'device' + str(device_to))
    if device_from == '1':
        driver.find_element(AppiumBy.ID, edit_ph_num_locator_1').send_keys(ph_num)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, call_button_locator_1).click()
    elif device_from == '2':
        driver.find_element(AppiumBy.ID, edit_ph_num_locator_2).send_keys(ph_num)
        driver.find_element(AppiumBy.ID, call_button_locator_2).click()
    elif device_from == '3':
        pass
    else:
        pass
    return driver


def end_call(device_to):
    if device_to == '1':
        desired_caps['udid'] = udid_1
        desired_caps['appActivity'] =main_activity_1
        desired_caps['appPackage'] = main_package_1
    elif device_to == '2':
        desired_caps['udid'] = udid_2
        desired_caps['appActivity'] =main_activity_2
        desired_caps['appPackage'] = main_package_2
    elif device_to == '3':
        pass
    elif device_to == '4':
        pass
    else:
        pass
    driver = webdriver.Remote(server, desired_caps)
    driver.open_notifications()
    driver.implicitly_wait(5)
    if device_to == '1':
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, end_call_locator_1).click()
        driver.implicitly_wait(2)

    elif device_to == '2':
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, end_call_locator_2).click()
        driver.implicitly_wait(2)

    return driver


def record_voicemail(driver,device):
    time.sleep(10)
    os.startfile(audiofile_path)
    time.sleep(5)
    if device == '1':
        driver.find_element(AppiumBy.ACCESSIBILITY_ID,end_call_locator_1).click()
    elif device == '2':
        driver.find_element(AppiumBy.ACCESSIBILITY_ID,end_call_locator_2).click()
    
    return driver
