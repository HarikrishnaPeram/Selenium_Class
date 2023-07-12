import pytest

@pytest.fixture()
def setUp():
    print("Run semo1 setup")
    yield
    print("Running demo2 teardown")


def test_demo1_methodA(setUp):
    print("Running demo1 method A")

def test_demo1_methodB(setUp):
    print("Running demo1 method B")
def test_demo1_methodC(setUp):
    print("Running demo1 method C")
