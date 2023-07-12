"""
File name should be start with test
test method name should start with test
py.test test_mod.py #run all tests below somepath
py.test test.module.py::test_method #any run test_method in test module
-s to print statements
-v verbose (To print results very clear)

"""
import pytest
@pytest.fixture()


def setUp():
    print("Run demo1 setup")
def test_demo1_methodA(setUp):
    print("Running demo1 method A")

def test_demo1_methodB(setUp):
    print("Running demo1 method B")
def test_demo1_methodC(setUp):
    print("Running demo1 method C")
def test_demo1_methodD(setUp):
    print("Running demo1 method D")
def test_demo1_methodE(setUp):
    print("Running demo1 method E")
#py.test -s -v test_case_demo1.py