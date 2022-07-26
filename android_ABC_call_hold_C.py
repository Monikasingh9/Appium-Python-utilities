
# This Functions puts Call C on hold while AB call continues
def hold_incoming_call_c(device):
    desired_caps = get_caps(excel_file, capabilities_sheet, device)
    desired_caps['appActivity'] = main_activity
    desired_caps['appPackage'] =main_app
    driver = webdriver.Remote(server, desired_caps)
    driver.open_notifications()
    driver.implicitly_wait(5)
    driver.find_element_by_accessibility_id('Accept').click()
    driver.implicitly_wait(10)
    dl = driver.find_elements(by=AppiumBy.CLASS_NAME,
                              value=action_list_locator)
    cnt = len(dl)
    for i in range(cnt):
        if (dl[i].text).startswith('Hold'):
            dl[i].click()
            break

    m = driver.find_element(by=AppiumBy.ID, value=merge_button_locator)
    verify = m.is_displayed()
    if verify is True:
        logging.info('call has been put on hold')
    else:
        logging.error('call could not be put on hold')
