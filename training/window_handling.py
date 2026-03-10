import time

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# ac = ActionChains(driver)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# parent = driver.current_window_handle
#
#
# ## scroll down till the end of the application
# ac.send_keys(Keys.END).perform()
# time.sleep(2)
#
# ## click on google+
# driver.find_element('xpath', '//a[text()="Google+"]').click()
# time.sleep(2)
#
# ##
# handles2 = driver.window_handles
# print(handles2)         ## [parent_window, child_window]
#
# for handle in handles2:
#     driver.switch_to.window(handle)
#     if "googleblog" in driver.current_url:
#         driver.find_element('xpath', '//input[@placeholder="Search blog"]').send_keys("Google pixel")
#         time.sleep(1)
#
#
# driver.switch_to.window(parent)
# time.sleep(1)
#
# driver.find_element('xpath', '//a[text()="YouTube"]').click()
# time.sleep(2)
#
# handles3 = driver.window_handles
# print(handles3)     ## [parent, child1, child2]
#
# for handle in handles3:
#     driver.switch_to.window(handle)
#     if 'youtube' in driver.current_url:
#         driver.find_element('xpath', '//input[@name="search_query"]').send_keys("python selenium")
#

#########################################################################################

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# ac = ActionChains(driver)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# parent = driver.current_window_handle
#
#
# ## scroll down till the end of the application
# ac.send_keys(Keys.END).perform()
# time.sleep(2)
#
# ## click on google+
# driver.find_element('xpath', '//a[text()="Google+"]').click()
# time.sleep(2)
#
# def handle_windows():
#     return driver.window_handles
#
# for handle in handle_windows():
#     driver.switch_to.window(handle)
#     if "googleblog" in driver.current_url:
#         driver.find_element('xpath', '//input[@placeholder="Search blog"]').send_keys("Google pixel")
#         time.sleep(1)
#
#
# driver.switch_to.window(parent)
# time.sleep(1)
#
# driver.find_element('xpath', '//a[text()="YouTube"]').click()
# time.sleep(2)
#
# for handle in handle_windows():
#     driver.switch_to.window(handle)
#     if 'youtube' in driver.current_url:
#         driver.find_element('xpath', '//input[@name="search_query"]').send_keys("python selenium")

#########################################################################################

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac = ActionChains(driver)

driver.get("https://www.myntra.com/")
time.sleep(2)

parent = driver.current_window_handle

home = driver.find_element('xpath', '//a[text()="Home"]')
ac.move_to_element(home).perform()
time.sleep(2)

driver.find_element('xpath', '//a[text()="Dinnerware & Serveware"]').click()
time.sleep(2)

driver.find_element('xpath', '//h4[@class="product-product"]').click()
time.sleep(2)

def handling_windows():
    return driver.window_handles

for handle in handling_windows():
    driver.switch_to.window(handle)
    if 'stainless-steel' in driver.current_url:
        driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
        time.sleep(2)

driver.switch_to.window(parent)
time.sleep(1)

driver.find_element('xpath', '(//h4[@class="product-product"])[2]').click()
time.sleep(2)


for handle in handling_windows():
    driver.switch_to.window(handle)
    if 'purple-colourblocked' in driver.current_url:
        driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()













































