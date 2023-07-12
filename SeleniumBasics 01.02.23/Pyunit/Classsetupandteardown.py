import unittest
class Testcasedemo2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("*#"*30)
        print("I will run only once before all tests")
        print("*#" * 30)
    #run before every test method
    def setUp(self):
        print("I will run once every Test Demo")

     # Test method

    def test_methodA(self):
        print("Running method A")

    def test_methodAA(self):
        print("Running method AA")

    def tearDown(self):
        print("I will run after every test demo")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("I will run only once before all tests")
        print("*#" * 30)