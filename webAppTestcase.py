import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Opens the wikipedia and sets the language as 'hi'
desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    browserName='Chrome'

)
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(5)
driver.get("http://wikipedia.com")

print(driver.title)

dropdown = driver.find_element(By.CSS_SELECTOR,"#searchLanguage")
select = Select(dropdown)
select.select_by_value("hi")
options = driver.find_elements(By.TAG_NAME,"option")
print(len(options))

for option in options:
    print ("Text is :", option.text , " Lang is :", option.get_attribute('lang'))

time.sleep(2)
driver.quit()
