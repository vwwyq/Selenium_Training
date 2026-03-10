'''
SYNCHRONIZATION :   Matching the speed of the webdriver to the speed of the web-application.

    There are 2 types of synchronization
    *   unconditional synchronization   :   No conditions are passed
            We achieve unconditional synchronization by passing time.sleep()
            This is a static wait.
            If we have given time.sleep(n), it will wait for the complete n seconds.
            So whenever there is a delay, we have to give time.sleep(n).
            Unnecessary wait is too much in unconditional synchronization

    *   conditional synchronization     :   Condition are passed
            There are 2 types
            *   implicit_wait   :   Conditions are internally given.
                        SYNTAX  :   driver.implicitly_wait(n).
                        Here, the wait is dynamic.
                        When there is a delay in loading the web-element, implicit_wait will make the driver wait for n seconds.
                        As soon as the element is available, it will perform the operations right away.
                        So no unnecessary wait.
                        One implicit_wait is sufficient for the whole program.
                        It will be applied globally.

            *   explicit_wait   :   Conditions are externally passed.
                        We achieve the synchronization by passing the conditions.

                        We have to import WebDriverWait and expected_conditions

                        from selenium.webdriver.support.ui import WebDriverWait
                        from selenium.webdriver.support import expected_conditions

                        wait_obj = WebDriverWait(driver, n)

                        wait_obj.until(expected_conditions.condition)

        WebDriverWait   :   It allows the driver to wait for a certain condition to check before we continue the operation.
                            Instead of waiting for a fixed amount of time, it waits until a condition is True or maximum time is reached.

        expected_conditions :   The conditions to be applied on the web-elements are already pre-defined and they are defined in expected_conditions.py
                            To make use of the pre-defined conditions we import expected_conditions

        until()         :   It is a method of WebDriverWait
                            It checks whether the given condition is satisfied or not
                            If the condition is True, it will continue the operations.
                            If the condition is False, it will always gives TimeOutException

'''


import time

''' 
Unconditional synchronization
Using time.sleep()
'''

## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files\loading.html')
# time.sleep(20)
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Ram')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Sharma')

# ################################################################################
#
''' 
Conditional synchronization
Using implicit_wait
'''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(30)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files\loading.html')
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Ram')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Sharma')


################################################################################

''' 
Conditional synchronization
Using explicit_wait
'''
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_obj = WebDriverWait(driver, 20)
#
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files\loading.html')
#
# wait_obj.until(EC.visibility_of_element_located(('xpath', '//div[contains(text(), "FirstName")]')))
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Ram')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Sharma')

# ###############################################################################################
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_obj = WebDriverWait(driver, 10)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('id', 'user-name').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('id', 'password').send_keys('secret_sauceeee')
# time.sleep(1)
# driver.find_element('id', 'login-button').click()
# time.sleep(3)
#
# try:
#     wait_obj.until(EC.url_contains("inventory"))
#     print("Valid credentials. Successfull login")
# except:
#     print("Invalid credentials. Unsuccessfull login")

# ###############################################################################################
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_obj = WebDriverWait(driver, 10)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('id', 'user-name').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('id', 'password').send_keys('secret_sauceeee')
# time.sleep(1)
# driver.find_element('id', 'login-button').click()
# time.sleep(3)
#
# try:
#     wait_obj.until(EC.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
#     print("Valid credentials. Successfull login")
# except:
#     print("Invalid credentials. Unsuccessfull login")

###############################################################################################

'''
fluent_wait :   A wait that waits for a maximum time
                Checks condition at regular intervals
                Ignores specific exceptions
                Check every few seconds until element appears or timeout happens
                Key Features:
                    Polling frequency
                    Timeout
                    Exception handling
                By default polling frequency is 5seconds
'''

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_obj = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[TimeoutException])

driver.get('https://www.saucedemo.com/')
time.sleep(2)

driver.find_element('id', 'user-name').send_keys('standard_user')
time.sleep(1)
driver.find_element('id', 'password').send_keys('secret_sauceeee')
time.sleep(1)
driver.find_element('id', 'login-button').click()
time.sleep(3)

try:
    wait_obj.until(EC.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
    print("Valid credentials. Successfull login")
except:
    print("Invalid credentials. Unsuccessfull login")













































































