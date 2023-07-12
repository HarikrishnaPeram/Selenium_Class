import unittest

from Pyunit.Assertdemo import TestCaseDemo
from Pyunit.SeleniumDemo import MyTestCases
from Pyunit.SeleniumDemo2 import MyTestCases1
from Pyunit.sample_demo import Testcasedemo2

#get all tests from Testclass1 and Testclass2
tc1=unittest.TestLoader(),loadTestsfromTestcase(MyTestCases)
tc2=unittest.TestLoader(),loadTestsfromTestcase(MyTestCases1)
tc3=unittest.TestLoader(),loadTestsfromTestcase(Testcasedemo2)
tc4=unittest.TestLoader(),loadTestsfromTestcase(TestCaseDemo)
#create a test suite combining estclass1 and Testclass2
smokeTest = unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner(verbosity=2).run(smokeTest)