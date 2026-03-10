'''
css selector    :   To locate the web-elements using any attribute, we go for css selector
                    SYNTAX  :   tagname[attr_name="attr_value"]

                    DRAWBACKS
                    *   Cant locate text using css selector
                    *   Indexing is not possible.
                        Incase of multiple occurances, css selector will always consider the first occurance

'''
import time

## Eg1

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
# driver.find_element("css selector", 'input[placeholder="Username"]').send_keys("standard_user")
# time.sleep(1)
# driver.find_element("css selector", 'input[placeholder="Password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('css selector', 'input[value="Login"]').click()
# time.sleep(3)
# driver.find_element('css selector', 'button[id="react-burger-menu-btn"]').click()
# time.sleep(2)
# driver.find_element('css selector', 'a[id="logout_sidebar_link"]').click()


############################################################################

## EG2

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://in.indeed.com/')
time.sleep(2)
driver.find_element('css selector', 'input[id="text-input-what"]').send_keys('software engineer')
time.sleep(1)
driver.find_element('css selector', 'input[id="text-input-where"]').send_keys('Bengaluru')
time.sleep(1)
driver.find_element('css selector', 'button[type="submit"]').click()

############################################################################

## Eg3

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
driver.find_element('css selector', 'input[type="text"]').send_keys("Ram")
time.sleep(1)
driver.find_element('css selector', 'input[type="text"]').send_keys('ram@gmail.com')

#####################################################################
























