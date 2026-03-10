import time

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Register"]').click()
# time.sleep(1)
# driver.find_element('id', 'gender-male').click()
# driver.find_element('id', 'FirstName').send_keys('Adithya')
# driver.find_element('id', 'LastName').send_keys('Mohla')
# driver.find_element('id', 'Email').send_keys('adi@gmail.com')
# driver.find_element('id', 'Password').send_keys('adi@12345')
# driver.find_element('id', 'ConfirmPassword').send_keys('adi@12345')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Log in"]').click()
# time.sleep(1)
# driver.find_element('id', 'Email').send_keys('adi@gmail.com')
# driver.find_element('id', 'Password').send_keys('adi@12345')

################################################################################


def outer(func):
    def wrapper(*args, **kwargs):
        print("Good morning")
        func(*args, **kwargs)
    return wrapper


@outer
def add(a, b):
    print(a + b)

add(10, 20)







































































