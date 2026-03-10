'''
Markers :   There are 2 types
            *   custom marker
            *   inbuilt marker

'''

import pytest

# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items / 2 deselected / 2 selected
# ## test_markers.py::test_reg       reg executing       PASSED
# ## test_markers.py::test_signup    signup executing    PASSED

######################################################################

# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"               -->     test_login and test_signup will execute
# ## pytest test_markers.py -vs -m="smoke"                -->     test_reg will execute
# ## pytest test_markers.py -vs -m="regression"           -->     test_logout will execute
# ## pytest test_markers.py -vs -m="sanity and smoke"     -->     None
# ## pytest test_markers.py -vs -m="sanity and regression"-->     None
# ## pytest test_markers.py -vs -m="smoke and regression" -->     None
# ## pytest test_markers.py -vs -m="sanity or smoke"      -->     test_login, test_reg and test_signup will execute
# ## pytest test_markers.py -vs -m="sanity or regression" -->     test_login, test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="smoke or regression"  -->     test_reg and test_logout will execute
# ## pytest test_markers.py -vs -m="not sanity"           -->     test_reg and test_logout will execute
# ## pytest test_markers.py -vs -m="not smoke"            -->     test_login, test_signup and test_logout will execute
# ## pytest test_markers.py -vs -m="not regression"       -->     test_login, test_signup and test_reg will execute

######################################################################

# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")

######################################################################
'''
skip    
'''


# @pytest.mark.skip
# def test_login():
#     print("login executing")
#
# def test_reg():
#     print("reg executing")
#
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.skip
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::test_login                         SKIPPED (unconditional skip)
# ## test_markers.py::test_reg       reg executing       PASSED
# ## test_markers.py::test_signup    signup executing    PASSED
# ## test_markers.py::test_logout                        SKIPPED (unconditional skip)

######################################################################

# @pytest.mark.skip
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::TestSample::test_login     SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_reg       SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_signup    SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_logout    SKIPPED (unconditional skip)

######################################################################

'''
skipif  :   
'''

# @pytest.mark.skipif(True, reason="login already executed")
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login SKIPPED (login already executed)

##----------------------------------------------------------------------

# @pytest.mark.skipif(False, reason="login already executed")
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login     login executing         PASSED

##----------------------------------------------------------------------

# @pytest.mark.skipif(reason="login already executed")
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login     SKIPPED (login already executed)

##----------------------------------------------------------------------

# @pytest.mark.skipif(True)
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login         ERROR

######################################################################

'''
xfail   :   
'''

# @pytest.mark.xfail
# def test_login():
#     raise Exception
#
# ## collected 1 item
# ## test_markers.py::test_login      XFAIL

##---------------------------------------------------------------

# @pytest.mark.xfail
# def test_login():
#     print("login")
#
# ## collected 1 item
# ## test_markers.py::test_login         login           XPASS

######################################################################

'''
paramterize     :   
'''

# @pytest.mark.parametrize("a, b", [(10, 20)])
# def test_add(a, b):
#     print(a + b)
#
# ## a, b --> (10, 20)    --> a=10, b=20
#
# ## collected 1 item
# ## test_markers.py::test_add[10-20]    30      PASSED

##--------------------------------------------------------------

# @pytest.mark.parametrize("a, b", [(10, 20), (1, 2), (10, -10), (1, 1)])
# def test_add(a, b):
#     print(a + b)

'''
a, b    --> (10, 20)    -->     a=10, b=20  --> 30
a, b    --> (1, 2)      -->     a=1, b=2    --> 3
a, b    --> (10, -10)   -->     a=10, b=-10 --> 0
a, b    --> (1, 1)      -->     a=1, b=1    --> 2
'''

## collected 4 items
## test_markers.py::test_add[10-20]    30      PASSED
## test_markers.py::test_add[1-2]      3       PASSED
## test_markers.py::test_add[10--10]   0       PASSED
## test_markers.py::test_add[1-1]      2       PASSED

##--------------------------------------------------------------

import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_obj = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[TimeoutException])


@pytest.mark.parametrize("username, password", [('standard_user', 'secret_sauce'), ('abcdefgh', '12345678')])
def test_login(username, password):
    driver.get('https://www.saucedemo.com/')
    time.sleep(2)
    driver.find_element('id', 'user-name').send_keys(username)
    time.sleep(1)
    driver.find_element('id', 'password').send_keys(password)
    time.sleep(1)
    driver.find_element('id', 'login-button').click()
    time.sleep(3)

    assert wait_obj.until(EC.visibility_of_element_located(('xpath', '//span[text()="Products"]')))






























































































































































