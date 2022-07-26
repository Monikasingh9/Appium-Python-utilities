# this file provides additional functions to automate actions that can be perfomed during A to B call 
# this is in continution to android_A2B_call.py


# This function puts the caller B on hold
def hold_call(device):
    driver = accept_call(device)
    driver.implicitly_wait(5)
    dl = driver.find_element(by=AppiumBy.XPATH,
                             value=hold_call_locator)
    dl.click()
    r = driver.find_element(by=AppiumBy.XPATH,
                            value=resume_call_locator)
    verify_connection = r.is_enabled()
    if verify_connection is True:
        logging.info('Call is on hold')
    else:
        logging.error('Call cannot be put on hold')
    return driver

    
#   This function adds a new caller to the ongoing A to B call
    def add_call(device):
    driver = accept_call(device,ph_num)
        dl = driver.find_element(by=AppiumBy.XPATH,
                             value=add_call_locator)
    dl.click()
    dial_a_number_by_copypaste_samsung(driver, ph_num)
    m = driver.find_element(by=AppiumBy.ID, value=merge_button_locator)
    verify = m.is_displayed()
    if verify is True:
        logging.info('Call has been added')
    else:
        logging.error('Call cannot be added')

        
# This function resumes the ongoing call
  def resume_call(device):
  driver = hold_call(device)
  r = driver.find_element(by=AppiumBy.XPATH,
                          value=resume_call_locator)
  r.click()
  driver.implicitly_wait(2)
  dl = driver.find_element(by=AppiumBy.XPATH,
                           value=hold_call_locator)

  verify_connection = dl.is_enabled()
  if verify_connection is True:
      logging.info('Call is resumed')
  else:
      logging.error('Call cannot be resumed')
