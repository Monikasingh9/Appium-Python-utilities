
import logging
from appium import webdriver
from configparser import ConfigParser


# reads the config file and gets the server and desired capabilities from config.ini

config = ConfigParser()
config.read("config.ini")
server = config.gt('Server', 'server_url')
desired_caps = {}
desired_caps['platformName'] = config.get('Desired Capabilities', 'platformName')
desired_caps['automationName'] = config.get('Desired Capabilities', 'automationName')
desired_caps['platformVersion'] = config.get('Desired Capabilities', 'platformVersion')
desired_caps['udid'] = config.get('Desired Capabilities', 'udid')
desired_caps['appPackage'] = config.get('Desired Capabilities', 'appPackage')
desired_caps['appActivity'] = config.get('Desired Capabilities', 'appActivity')


# opens the target app on the device

def open_app():
    driver = webdriver.Remte(server, desired_caps)
    return driver

# gets all the device information-androidId,apiVersion,bluetooth,brand,carrierName,displayDensity,
# locale,manufacturer,model,networks,platformVersion,realDisplaySize,timeZone

def get_device_info(info_type):
    d = open_app()
    l = d.execute_script('mobile:deviceInfo')
    mylist = []
    for i in l.keys():
        if i == info_type == 'networks':
            le = len(l[i])
            print(le)
            for j in l[i]:
                mylist.append(j.values())
                return mylist
        elif i == info_type:
            return (l[i])
        else:
            logging.ERROR('Wrong info type: info types supported are -androidId,apiVersion,bluetooth,brand,carrierName,'
                          'displayDensity,locale,manufacturer,model,networks,platformVersion,realDisplaySize,timeZone')


l = get_device_info('networks')
print(l)
