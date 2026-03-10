'''
The operations which are performed using mouse/keyboard, we call them as low-level operations.
The operations such as hovering, right click, double click, scrolling operations, drag and drop operations,
enter key, ctrl, backspace, delete,...


To perform low-level operations in selenium, we use ActionChains

'''

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac = ActionChains(driver)

##----------------------------------------------------------------------------

'''     mouse hovering operations       '''

# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# men = driver.find_element('xpath', '(//a[text()="Men"])[1]')
# ac.move_to_element(men).perform()
# time.sleep(2)
#
# women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
# ac.move_to_element(women).perform()
# time.sleep(2)
#
# kids = driver.find_element('xpath', '(//a[text()="Kids"])[1]')
# ac.move_to_element(kids).perform()
# time.sleep(2)
#
# home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
# ac.move_to_element(home).perform()

##----------------------------------------------------------------------------

'''     Double click        '''
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ele1 = driver.find_element('xpath', '//button[text()="Copy Text"]')
# ac.double_click(ele1).perform()
# time.sleep(2)
#
# ele2 = driver.find_element('xpath', '//label[text()="Name:"]')
# ac.double_click(ele2).perform()


#################################################################################

'''     Right click        '''

# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ac.context_click().perform()

##--------------------------------------------------------------------

# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="Dynamic Button"]')
#
# ac.context_click(ele).perform()

#################################################################################

'''     SCROLLING OPERATIONS        '''


# ## Scroll to specific element
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# ref_ele = driver.find_element('xpath', '//div[text()=" POPULAR SEARCHES "]')
# ac.scroll_to_element(ref_ele).perform()

##------------------------------------------------------------------------------

# ## To scroll to the end of the application
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
# ac.send_keys(Keys.END).perform()
# time.sleep(2)
#
# ## To go back to the start of the application
# ac.send_keys(Keys.HOME).perform()

##------------------------------------------------------------------------------

# ## page_down and page_up scrolling
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
# ac.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac.send_keys(Keys.PAGE_UP).perform()

##------------------------------------------------------------------------------

# ## scroll_by_amount
#
# driver.get("https://www.myntra.com/")
# time.sleep(2)
# ac.scroll_by_amount(0, 2000).perform()      ## Will scroll down by 2000 pixels
# time.sleep(2)
# ac.scroll_by_amount(0, -2000).perform()            ## Will scroll up by 2000 pixels

#################################################################################

'''     DRAG AND DROP       '''

# ## drag and drop
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac.scroll_to_element(ele).perform()
# time.sleep(2)
#
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
# droppable_ele = driver.find_element('xpath', '//div[@id="droppable"]')
#
# ac.drag_and_drop(draggable_ele, droppable_ele).perform()

##----------------------------------------------------------------------------

# ## drag and drop by offset
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac.scroll_to_element(ele).perform()
# time.sleep(2)
#
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
#
# ac.drag_and_drop_by_offset(draggable_ele, 50, 50).perform()

######################################################################################

# ## slider
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac.scroll_to_element(ele).perform()
# time.sleep(2)
#
# left_pointer = driver.find_element('xpath', '//div[@id="slider-range"]/span[1]')
#
# ac.click_and_hold(left_pointer).move_by_offset(50, 0).release().perform()
# time.sleep(2)
# ac.click_and_hold(left_pointer).move_by_offset(-50, 0).release().perform()

######################################################################################

# ## ctrl + A
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# ac.key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform()

######################################################################################

# ## tab
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="name"]').send_keys("Ram")
# time.sleep(1)
# ac.send_keys(Keys.TAB).perform()            ## Will  shift the cursor to the nexr textbox
# time.sleep(2)
#
# ac.send_keys("ram@gmail.com").perform()














































