'''
What is Headless Execution?
Headless execution means running browser automation without opening the browser UI.
The browser runs in the background.


Example:
    Normally Selenium opens:
    Chrome → UI visible
    In headless mode:
    Chrome runs → no window opens

Advantages
    Faster test execution
    Less memory usage
    Ideal for automation pipelines
    Can run on servers without GUI
Disadvantages
    Harder to debug
    Some UI-related tests may behave differently
'''


import time


# ## Chrome
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--headless")
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
# driver.find_element('id', 'name').send_keys("Ram")
# time.sleep(1)
# driver.find_element('id', 'email').send_keys('ram@gmail.com')
# time.sleep(1)
# driver.find_element('id', 'phone').send_keys('9080705060')
# time.sleep(1)
# driver.find_element('id', 'textarea').send_keys('Bhuvaneshwar')
# time.sleep(1)
# driver.find_element('id', 'maleeeeee').click()
# time.sleep(1)
# driver.find_element('id', 'monday').click()

############################################################################

## Firefox

from selenium import webdriver

opts = webdriver.FirefoxOptions()
opts.add_argument("--headless")

driver = webdriver.Firefox(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
driver.find_element('id', 'name').send_keys("Ram")
time.sleep(1)
driver.find_element('id', 'email').send_keys('ram@gmail.com')
time.sleep(1)
driver.find_element('id', 'phone').send_keys('9080705060')
time.sleep(1)
driver.find_element('id', 'textarea').send_keys('Bhuvaneshwar')
time.sleep(1)
driver.find_element('id', 'maleeeeee').click()
time.sleep(1)
driver.find_element('id', 'monday').click()
















