import time

'''

*   get()               :   To launch the web-application, we use get()
                SYNTAX  :   driver.get("url")

*   maximize_window()   :   This will maximize the browser window
                SYNTAX  :   driver.maximize_window()

*   minimize_window()   :   This will minimize the browser window
                SYNTAX  :   driver.minimize_window()

*   back()              :   This will go back()
                SYNTAX  :   driver.back()

*   forward()           :   This will go forward
                SYNTAX  :   driver.forward()

*   refresh()           :   This will refresh the page
                SYNTAX  :   driver.refresh()

*   current_url         :   This is a property. It will give the url of the page
                SYNTAX  :   driver.current_url

*   title               :   This is a property. It will give the title of the page
                SYNTAX  :   driver.title

*   name                :   This is a property. It will give the name of the browser we've used in the code
                SYNTAX  :   driver.name

*   close()             :   It will close the browser object
                SYNTAX  :   driver.close()

'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

## launch the application
driver.get("https://www.myntra.com/")
time.sleep(2)

## to maximize the window
driver.maximize_window()
time.sleep(2)

# ## to minimize the window
# driver.minimize_window()

## To go back
driver.back()
time.sleep(2)

## To go forward
driver.forward()
time.sleep(2)

## To refresh
driver.refresh()

## current_url
print(driver.current_url)

## title
print(driver.title)

## name
print(driver.name)

## page_source
print(driver.page_source)

##--------------------------------------------------------------------------

## To take the screenshots

# driver.save_screenshot("myntra_homepage.png")
## The screenshot will be saved in the same package as our python file


## To save the screenshots in different location
# driver.save_screenshot(r'C:\Users\Ramya\PycharmProjects\Sel-A13-Dec26-2025\screenshots\myn_ss.png')

##--------------------------------------------------------------------------

driver.close()




















