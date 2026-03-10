import time

from selenium import webdriver
from ddt.read_excel import excel_data

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

data = excel_data()
## {'firstname': 'Adithya', 'lastname': 'Mohla', 'email_id': 'adithya@gmail.com', 'password': 'adithya@123', 'confirm_pwd': 'adithya@123'}

driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

driver.find_element('xpath', '//a[text()="Register"]').click()
time.sleep(1)
driver.find_element('id', 'gender-male').click()
driver.find_element('id', 'FirstName').send_keys(data['firstname'])
driver.find_element('id', 'LastName').send_keys(data['lastname'])
driver.find_element('id', 'Email').send_keys(data['email_id'])
driver.find_element('id', 'Password').send_keys(data['password'])
driver.find_element('id', 'ConfirmPassword').send_keys(data['confirm_pwd'])











































































