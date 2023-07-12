import unittest


class TestCaseDemo(unittest.TestCase):
        def test_assertTrueFalse(self):
            a=True
            self.assertTrue(a,"a is not false")
            b=False
            self.assertTrue(b,"b is not True")
        def test_assertequal(self):
            a="test"
            b="test"
            self.assertEqual(a,b, msg="a is equal to b")