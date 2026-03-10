import time

class TestRegister:

    def test_reg_link(self, setup):
        setup.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(1)

    def test_gender_btn(self, setup):
        setup.find_element('id', 'gender-male').click()

    def test_fname(self, setup):
        setup.find_element('id', 'FirstName').send_keys('Adithya')

    def test_lname(self, setup):
        setup.find_element('id', 'LastName').send_keys('Mohla')

    def test_reg_email(self, setup):
        setup.find_element('id', 'Email').send_keys('adi@gmail.com')

    def test_reg_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('adi@12345')

    def test_confirm_pwd(self, setup):
        setup.find_element('id', 'ConfirmPassword').send_keys('adi@12345')
        time.sleep(2)
