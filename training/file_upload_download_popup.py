import time


'''     Uploading single file       '''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# file1 = r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files\css_selector.html'
#
# driver.find_element('xpath', '//input[@id="singleFileInput"]').send_keys(file1)
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Upload Single File"]').click()

##############################################################################################

'''     Uploading Multiple files       '''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# time.sleep(2)
#
# file1 = r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files\css_selector.html'
# file2 = r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files\demo.html'
# file3 = r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files\loading.html'
# file4 = r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files\progressbar.html'
#
# driver.find_element('xpath', '//input[@id="multipleFilesInput"]').send_keys(f'{file1}\n{file2}\n{file3}\n{file4}')
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Upload Multiple Files"]').click()

####################################################################################################

'''     File download popup     '''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
# driver.get("https://demoqa.com/upload-download")
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Download"]').click()
# ## The file will be downloaded in the default downloads folder

##----------------------------------------------------------------------

'''     To download the files in different location     '''


# ## Chrome
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# prefs = {
#     "download.default_directory": r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files',
#     "download.prompt_for_download":False,
#     "safebrowsing.enabled":True,
#     "plugins.always_open_pdf_externally":True
# }
#
# opts.add_experimental_option("prefs", prefs)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
#
# driver.get("https://demoqa.com/upload-download")
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Download"]').click()

##---------------------------------------------------------------

## Firefox
from selenium import webdriver

opts = webdriver.FirefoxOptions()

opts.set_preference("browser.download.folderList", 2)
opts.set_preference("browser.download.dir", r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\locators_')

driver = webdriver.Firefox(opts)
driver.implicitly_wait(10)


driver.get("https://demoqa.com/upload-download")
time.sleep(2)

driver.find_element('xpath', '//a[text()="Download"]').click()























































































