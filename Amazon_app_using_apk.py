
from pathlib import Path
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# This program opens the amazon using te apk file and if it is not installed then it install it and then pens it
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'
desired_caps['app'] = str(Path().absolute().parent) + '\\App\\Amazon.apk'
desired_caps['appWaitActivity']='com.amazon.mShop.navigation.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(5)

driver.find_element(AppiumBy.ID,'in.amazon.mShop.android.shopping:id/sso_continue').click()
driver.find_element(AppiumBy.ID,"in.amazon.mShop.android.shopping:id/chrome_search_hint_view").click()
driver.find_element(AppiumBy.ID,"in.amazon.mShop.android.shopping:id/rs_search_src_text").send_keys("books")
list = driver.find_elements(AppiumBy.ID,"in.amazon.mShop.android.shopping:id/iss_search_suggestions_list_view")
print(list)

driver.quit()
