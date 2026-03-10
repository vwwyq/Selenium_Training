'''

A ListBox is a web element that allows users to select one or more options from a list
If the tagname of the dropdown/listbox is "select", then it is a standard listbox

Selenium provides a class called Select to interact with <select> elements.

There are 2 types
*   single select listbox   :   If we can select only one element from the dropdown, then it is a single select listbox
*   multi select listbox    :   If we can select multiple elements from the dropdown, then it is a multi select listbox

We will handle single-select and multi-select listboxes in the same way

from selenium.webdriver.support.select import Select
    select_obj = Select(listbox_having_select_tag)

    We have 3 attributes to select the elements from the dropdown
    *   select_by_index     :   Will select the element from the dropdown by passing the index number
                                SYNTAX  :   select_obj.select_by_index(index_num)
                                Index number starts from 0
                                If the index number is out of range, then it will give NoSuchElementException
                                If we dont give any index number, it will give -->
                                        TypeError: Select.select_by_index() missing 1 required positional argument: 'index'

    *   select_by_value     :   Will select the element from the dropdown by passing the value of the value attribute
                                SYNTAX  :   select_obj.select_by_value("value")

    *   select_by_visible_text  :   Will select the element from the dropdown by passing the text
                                SYNTAX  :   select_obj.select_by_visible_text("text")


    We have 3 attributes to deselect the elements from the dropdown
    *   deselect_by_index     :   Will deselect the element which is present in that index number
                                SYNTAX  :   select_obj.deselect_by_index(index_num)

    *   deselect_by_value     :   Will deselect the element of the value passed
                                SYNTAX  :   select_obj.deselect_by_value("value")

    *   deselect_by_visible_text  :   Will deselect the element having the given text
                                SYNTAX  :   select_obj.deselect_by_visible_text("text")


    *   select_obj.deselect_all()   :   This will deselect all the selected elements


'''

import time

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files\demo.html')
# time.sleep(2)
#
# listbox = driver.find_element('xpath', '//select[@id="standard_cars"]')
# select_obj = Select(listbox)

# ## select_by_index
# select_obj.select_by_index(5)
# time.sleep(2)
# select_obj.select_by_index(9)
# time.sleep(2)
# select_obj.select_by_index(1)

# ## select_by_value
# select_obj.select_by_value("bmw")
# time.sleep(1)
# select_obj.select_by_value("lr")
# time.sleep(1)
# select_obj.select_by_value("min")


# ## select_by_visible_text
# select_obj.select_by_visible_text("Ford")
# time.sleep(1)
# select_obj.select_by_visible_text("Mercedes")
# time.sleep(1)
# select_obj.select_by_visible_text("Toyota")

#################################################################################

'''     Multi-select listbox        '''

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files\demo.html')
# time.sleep(2)
#
# listbox = driver.find_element('xpath', '//select[@id="multiple_cars"]')
# select_obj = Select(listbox)

##--------------------------------------------------------------------------------

# ## select_by_index
# select_obj.select_by_index(1)
# time.sleep(1)
# select_obj.select_by_index(2)
# time.sleep(1)
# select_obj.select_by_index(3)
# time.sleep(2)
#
# ## deselect_by_index
# select_obj.deselect_by_index(1)
# time.sleep(1)
# select_obj.deselect_by_index(2)
# time.sleep(1)
# select_obj.deselect_by_index(3)

##--------------------------------------------------------------------------------

# ## select_by_value
# select_obj.select_by_value("aud")
# time.sleep(1)
# select_obj.select_by_value("for")
# time.sleep(1)
# select_obj.select_by_value("jgr")
# time.sleep(2)
#
# ## deselect_by_value
# select_obj.deselect_by_value("aud")
# time.sleep(1)
# select_obj.deselect_by_value("for")
# time.sleep(1)
# select_obj.deselect_by_value("jgr")


##--------------------------------------------------------------------------------

# ## select_by_visible_text
# select_obj.select_by_visible_text("Honda")
# time.sleep(1)
# select_obj.select_by_visible_text("Jaguar")
# time.sleep(1)
# select_obj.select_by_visible_text("Land Rover")
# time.sleep(2)
#
#
# ## deselect_by_visible_text
# select_obj.deselect_by_visible_text("Honda")
# time.sleep(1)
# select_obj.deselect_by_visible_text("Jaguar")
# time.sleep(1)
# select_obj.deselect_by_visible_text("Land Rover")

##-----------------------------------------------------------------------

# select_obj.select_by_visible_text("Honda")
# time.sleep(1)
# select_obj.select_by_visible_text("Jaguar")
# time.sleep(1)
# select_obj.select_by_visible_text("Land Rover")
# time.sleep(2)
#
# select_obj.deselect_all()

##-----------------------------------------------------------------------

'''     
is_multiple :   
'''

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files\demo.html')
# time.sleep(2)
#
# listbox1 = driver.find_element('xpath', '//select[@id="standard_cars"]')
# select1 = Select(listbox1)
#
# listbox2 = driver.find_element('xpath', '//select[@id="multiple_cars"]')
# select2 = Select(listbox2)
#
# print(select1.is_multiple)      ## None
# print(select2.is_multiple)      ## True


################################################################################################

'''
all_selected_options
'''

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files\demo.html')
# time.sleep(2)
#
# listbox = driver.find_element('xpath', '//select[@id="multiple_cars"]')
# select_obj = Select(listbox)

# select_obj.select_by_index(3)
# time.sleep(1)
# select_obj.select_by_index(2)
# time.sleep(1)
# select_obj.select_by_index(1)
# time.sleep(2)

##-----------------------------------------------------------------------------------

# all_options = select_obj.all_selected_options
# # print(all_options)          ## list of web-elements         ## [wb1, wb2, wb3]
#
# for ele in all_options:
#     print(ele.text)

##----------------------------------------------------------------------------------

# first = select_obj.first_selected_option
# print(first.text)

##----------------------------------------------------------------------------------

# ## options
# all_elements = select_obj.options
# # print(all_elements)         ## list of web-elements
#
# for ele in all_elements:
#     print(ele.text)

############################################################################################

'''     NORMAL LISTBOXES        '''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://www.irctc.co.in/nget/train-search")
time.sleep(2)

driver.find_element('xpath', '//button[text()="OK"]').click()
time.sleep(2)

driver.find_element('xpath', '(//div[@role="button"])[1]').click()
time.sleep(2)

driver.find_element('xpath', '//span[text()="Vistadome Chair Car (VC)"]').click()
time.sleep(2)

driver.find_element('xpath', '(//div[@role="button"])[2]').click()
time.sleep(2)

driver.find_element('xpath', '//span[text()="TATKAL"]').click()





































