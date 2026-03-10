'''
id  :   id is an attribute which is also a locator.
        Whenever we have id attribute, we can go for id locator

        *   Whenever we are having multiple occurances, id will always consider the first occurance

'''



import time

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.saucedemo.com/")
# time.sleep(2)
#
# username = driver.find_element("id", "user-name")
# print(username)
#
# pwd = driver.find_element('id', 'password')
# print(pwd)
#
# login_btn = driver.find_element('id', 'login-button')
# print(login_btn)
#
#
# username.send_keys("standard_user")
# time.sleep(1)
# pwd.send_keys("secret_sauce")
# time.sleep(1)
# login_btn.click()

#####################################################################

## EG1

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.saucedemo.com/")
# time.sleep(2)
#
# driver.find_element("id", "user-name").send_keys("standard_user")
# time.sleep(1)
# driver.find_element('id', 'password').send_keys("secret_sauce")
# time.sleep(1)
# driver.find_element('id', 'login-button').click()
# time.sleep(3)
# driver.find_element('id', 'react-burger-menu-btn').click()
# time.sleep(2)
# driver.find_element('id', 'logout_sidebar_link').click()

###############################################################################

## EG2

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

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
driver.find_element('id', 'male').click()
time.sleep(1)
driver.find_element('id', 'monday').click()

############################################################################

## EG3

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/register")
# time.sleep(2)
#
# driver.find_element("id", "gender-male").click()
# time.sleep(1)
# driver.find_element("id", "FirstName").send_keys('Rohit')
# time.sleep(1)
# driver.find_element("id", "LastName").send_keys("Shukla")
# time.sleep(1)
# driver.find_element("id", "Email").send_keys('rohit@gmail.com')
# time.sleep(1)
# driver.find_element("id", "Password").send_keys('rohit@12345')
# time.sleep(1)
# driver.find_element("id", "ConfirmPassword").send_keys('rohit@12345')




































































