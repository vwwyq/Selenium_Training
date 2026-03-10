'''
FIXTURES    :   It is a function block which hold the common functionality.
                It is an inbuilt decorator which is used to perform setup and teardown operations

                setup       :   The set of operations which executes before the execution of the test_function
                teardown    :   The set of operations which executes after the execution of the test_function

                SYNTAX  :   @pytest.fixture([autouse])
                            def func():
                                pass            ## setup
                                yield
                                pass            ## teardown

                            def test_func(func):
                                pass

                            We should pass the name of the fixture as a parameter for the test_function

                Fixtures helps in
                    *   Avoiding the code duplication
                    *   helps in reusability
                    *   We dont have to modify the main functions when we use fixtures

                Fixtures have some optional parameters
                *   autouse     :   When we give autouse=True,
                                    By default the fixture will be applied for all the test_functions in that module.
                                    Without passing the name of a fixture as a parameter for the test_function, we can still by apply
                                    the fixtures to the test_functions by declaring autouse=True

                *   scope   :   It is an argument of a fixture. It is also an optional parameter.
                                scope defines the scope of a fixture.

                                When we give scope="class", the fixture will be applied on a class level.
                                Before the execution of the entire class, setup operation will be performed
                                After the execution of the entire class, teardown operation will be performed

                                When we give scope="module", the fixture will be applied on a module(file) level.
                                Before the execution of the entire module, setup operation will be performed
                                After the execution of the entire module, teardown operation will be performed

                                Be default, scope="function"


'''


# def outer(func):
#     def wrapper(*args, **kwargs):
#         print("Good morning")
#         func(*args, **kwargs)
#     return wrapper
#
#
# @outer
# def add(a, b):
#     print(a + b)
#
# add(10, 20)

###############################################################################
import pytest

#
# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 2 items
# ## test_fixtures.py::test_login    Good morning    login executing     PASSED
# ## test_fixtures.py::test_logout   Good morning    logout executing    PASSED

###############################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login        Good morning        login executing     PASSED
# ## test_fixtures.py::test_signup                           signup executing    PASSED
# ## test_fixtures.py::test_logout       Good morning        logout executing    PASSED

###############################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup(greet):
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")
#
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning    login executing     PASSEDGood evening
# ## test_fixtures.py::test_signup   Good morning    signup executing    PASSEDGood evening
# ## test_fixtures.py::test_logout   Good morning    logout executing    PASSEDGood evening

'''
The operations before yield will execute before the execution of the test_function
The operations after yield will execute after the execution of the test_function
'''

###############################################################################
#
# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning    login executing     PASSEDGood evening
# ## test_fixtures.py::test_signup   Good morning    signup executing    PASSEDGood evening
# ## test_fixtures.py::test_logout   Good morning    logout executing    PASSEDGood evening

###############################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self, greet):
#         print("login executing")
#
#     def test_signup(self, greet):
#         print("signup executing")
#
#     def test_logout(self, greet):
#         print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning    login executing     PASSEDGood evening
# ## test_fixtures.py::test_signup   Good morning    signup executing    PASSEDGood evening
# ## test_fixtures.py::test_logout   Good morning    logout executing    PASSEDGood evening

###############################################################################

# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning    login executing     PASSEDGood evening
# ## test_fixtures.py::test_signup   Good morning    signup executing    PASSEDGood evening
# ## test_fixtures.py::test_logout   Good morning    logout executing    PASSEDGood evening

###############################################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::TestSample::test_login    Good morning    login executing     PASSED
# ## test_fixtures.py::TestSample::test_signup                   signup executing    PASSED
# ## test_fixtures.py::TestSample::test_logout                   logout executing    PASSEDGood evening

###############################################################################

'''
scope is the parameter of the fixture.
When we give scope='class', the fixture will be applied on a class level.
*   It will perform the setup operation.
*   It will execute all the attributes of the TestClass
*   It will perform the teardown operation
'''

###############################################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# class TestExample:
#
#     def test_gmail(self):
#         print("gmail executing")
#
#     def test_yahoo(self):
#         print("yahoo executing")
#
#     def test_reg(self):
#         print("reg executing")
#
# ## collected 6 items
# ## test_fixtures.py::TestSample::test_login    Good morning    login executing     PASSED
# ## test_fixtures.py::TestSample::test_signup                   signup executing    PASSED
# ## test_fixtures.py::TestSample::test_logout                   logout executing    PASSEDGood evening
# ## test_fixtures.py::TestExample::test_gmail   Good morning    gmail executing     PASSED
# ## test_fixtures.py::TestExample::test_yahoo                   yahoo executing     PASSED
# ## test_fixtures.py::TestExample::test_reg                     reg executing       PASSEDGood evening

###############################################################################

# @pytest.fixture(autouse=True, scope='module')
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# class TestExample:
#
#     def test_gmail(self):
#         print("gmail executing")
#
#     def test_yahoo(self):
#         print("yahoo executing")
#
#     def test_reg(self):
#         print("reg executing")
#
# ## collected 6 items
# ## test_fixtures.py::TestSample::test_login    Good morning    login executing     PASSED
# ## test_fixtures.py::TestSample::test_signup                   signup executing    PASSED
# ## test_fixtures.py::TestSample::test_logout                   logout executing    PASSED
# ## test_fixtures.py::TestExample::test_gmail                   gmail executing     PASSED
# ## test_fixtures.py::TestExample::test_yahoo                   yahoo executing     PASSED
# ## test_fixtures.py::TestExample::test_reg                     reg executing       PASSEDGood evening

###############################################################################

import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Chrome(opts)
    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(2)
    yield driver
    driver.close()

## setup --> webdriver.Chrome(opts)

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

class TestLogin:

    def test_login_link(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self, setup):
        setup.find_element('id', 'Email').send_keys('adi@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('adi@12345')













































































































