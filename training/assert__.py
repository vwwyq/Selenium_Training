'''
assert  :   It is a keyword.
            It is used to validate the expected output with the actual output.
            assert will take a condition

            SYNTAX  :   assert condition

            If the condition is True, the test case passes and the execution will continue
            If the condition is False, then it will always give AssertionError
'''


# assert 10%2==0
# print("Good afternoon")

##----------------------------------------------------

# assert 11%2==0, "condition is False"
# print("Good afternoon")
#
# ## AssertionError

############################################################################################
'''
assert not
'''

# a = 10

# assert a>5      ## assert 10>5 --> assert True --> True

# assert not a>5      ## assert not 10>5 --> assert not True --> assert False --> AssertionError

############################################################################################

'''
assert actual==expected
'''

# a = 10
# b = 10
#
# assert a==b        ## assert 10==10     --> assert True --> True

##-------------------------

# a = 10
# b = 20
#
# assert a==b     ## assert 10==20  --> assert False --> AssertionError

############################################################################################

'''
assert actual != expected
'''
# a = 10
# b = 10
#
# assert a!=b     ## assert 10!=10 -->    assert False --> AssertionError

############################################################################################

'''
assert value is None
'''

assert None     ## AssertionError
















































































