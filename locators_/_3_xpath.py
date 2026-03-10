'''
xpath   :   It is a locator to locate any element on the application uniquely.
            Using xpath, we can locate the web elements using attributes, using text, can do indexing, can locate
            dynamically changing elements.
            We can locate any element on the application using xpath

            There are 2 types of xpath
            *   Absolute xpath  :   Starts from the root of html
                                    We use / to write the absolute xpath
                                    / represents immediate child

                                    DRAWBACKS
                                    *   Depends on the full path from the root
                                    *   Difficult to maintain
                                    *   Not reusable
                                    *   Not readable
                                    *   Very lengthy and time consuming

            *   Relative xpath  :   Doesnot start from the root of html
                                    We use // to write relative xpath
                                    // represents any child

'''

import time

# ## EG1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A13-Dec26-2025\files\css_selector.html')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/table[2]/tbody/tr[1]/td/input').send_keys('Rohit')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/table[2]/tbody/tr[2]/td/input').send_keys('rohi@12345')

####################################################################################################
## Eg2

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/input').click()

####################################################################################################

'''
attribute name and value    :   //tagname[@attr_name="attr_value"]
'''

# ## EG1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="user-name"]').send_keys("standard_user")
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="login-button"]').click()
# time.sleep(3)
# driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@id="logout_sidebar_link"]').click()

##############################################################################

## EG2

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
# driver.find_element('xpath', '//a[@data-group="men"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@data-group="kids"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@data-group="beauty"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@data-group="genz"]').click()

##############################################################################

''' GROUP INDEXING'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A13-Dec26-2025\files\css_selector.html')
# time.sleep(2)
#
# driver.find_element('xpath', '(//input[@name="fname"])[1]').send_keys('Sheeta')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@name="fname"])[2]').send_keys('Praveen')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@name="fname"])[3]').send_keys('Tushar')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@name="mname"])[1]').send_keys('Tejas')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@name="mname"])[2]').send_keys('Vani')

##----------------------------------------------------------------------------

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//input[@type="text"])[1]').send_keys('Ram')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[2]').send_keys('ram@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[3]').send_keys('9080704050')

##------------------------------------------------------------------------

'''
text()  :   //tagname[text()="text"]
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://x.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Create account"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//button[@aria-label="Close"]').click()
# time.sleep(3)
# driver.find_element('xpath', '//span[text()="Sign in"]').click()

##------------------------------------------------------------------------

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Women"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Beauty"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Genz"]').click()


##############################################################################

'''
contains    :   To locate the webelement using partial text of any tagname 
                SYNTAX  :   //tagname[contains(text(), "partial_text")]

'''

# ## EG1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://selectorshub.com/')
# time.sleep(2)
# driver.find_element('xpath', '(//span[contains(text(), "Products")])[1]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "Courses")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "Practice Page")]').click()

#######################################################################################

# ## EG2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.kushals.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[contains(text(), "Bangles")])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Wedding Store")])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Happy Customers")])[2]').click()

#########################################################################################

'''
dependent independent xpath
    *   identify the dependent independent element
    *   write the xpath of the independent element
    *   Traverse back until we get the common match for dependent independent element\
    *   continue writing the xpath of the dependent element

'''

## Eg1

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.python.org/")
time.sleep(2)

driver.find_element('xpath', '(//a[text()="Downloads"])[1]').click()
time.sleep(2)

driver.find_element('xpath', '//a[text()="Python 3.13.11"]/../..//a[text()="Release notes"]').click()

###############################################################################

## Eg2

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)

# driver.get("https://www.iforex.in/tools/live-rates")
# time.sleep(2)
#
# driver.find_element('xpath', '//div[@id="ai-chat-close"]').click()
# time.sleep(5)

# gold_sellprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[2]')
# print(f'The sellprice of gold is {gold_sellprice.text}')
#
# buy_sellprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[3]')
# print(f'The buyprice of gold is {buy_sellprice.text}')

# for i in range(1, 20, 2):
#     gold_sellprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[2]')
#     print(f'The sellprice of gold is {gold_sellprice.text}')
#
#     buy_sellprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[3]')
#     print(f'The buyprice of gold is {buy_sellprice.text}')
#
#     time.sleep(2)

###############################################################################

## Eg3

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)

# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files\demo.html')
# time.sleep(2)
# driver.find_element('xpath', '//td[text()="Ruby"]/..//input[@name="download"]').click()








































































