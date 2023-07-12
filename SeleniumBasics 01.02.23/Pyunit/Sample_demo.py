#run Before every testmethod
import unittest


class Testcasedemo2(unittest.TestCase):

    def setUp(self):
        print("I will run once every Test Demo")

    # Test method

    def test_methodA(self):
        print("Running method A")

    def test_methodAA(self):
        print("Running method AA")

    def test_methodB(self):
        print("Running method B")

    def test_methodC(self):
        print("Running method C")

    def test_methodD(self):
        print("Running method D")

    def test_methodE(self):
        print("Running method E")

    def test_methodF(self):
        print("Running method F")

    # Run After every test method
    def tearDown(self):
        print("I will run every test demo")

    if __name__ == '__main__':
        unittest.main(verbosity=2)
    # Command to run the test in terminal
    # python -m unittest sample_demo.py