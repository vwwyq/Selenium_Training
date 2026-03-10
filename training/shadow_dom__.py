'''
What is Shadow DOM?
Shadow DOM is a technique used in modern web applications to encapsulate HTML elements and CSS.
It means the elements are hidden inside another DOM structure, so Selenium cannot directly locate them using normal locators.

Why Shadow DOM is Used
    Developers use Shadow DOM for:
    Encapsulation of UI components
    Avoid CSS conflicts
    Reusable components
    Used in modern frameworks

'''

import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get("https://the-internet.herokuapp.com/shadowdom")
time.sleep(2)

shadow_ele = driver.find_element("css selector", "my-paragraph")
host = shadow_ele.shadow_root
data = host.find_element('css selector', 'p')
print(data.text)




































































