from multiprocessing.sharedctypes import Value
import unittest
import calc


# args for testcalc are what it inherits from (testcalc inherits unittest.testcase)
class TestCalc(unittest.TestCase):

    def test_add(self):  # required naming convention (must start with test_)

        # using inherited method assertEqual we can check whether the result of our function
        # is equal to the expected value
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-10, -5), -15)
        self.assertEqual(calc.add(-10, 5), -5)
        # the three test methods here are part of the 1 test

    def test_subtract(self):
        self.assertEqual(calc.subtract(-10, -5), -5)
        self.assertEqual(calc.subtract(-10, 5), -15)
        self.assertEqual(calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 2), 6)
        self.assertEqual(calc.multiply(-3, 2), -6)
        self.assertEqual(calc.multiply(-3, -2), 6)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-10, 5), -2)
        self.assertEqual(calc.divide(10, -5), -2)
        self.assertEqual(calc.divide(10, 4), 2.5)
        self.assertEqual(calc.divide(10, -4), -2.5)

        """ (exception, function, each arg for the function)
        otherwise the function will throw the error and the test will think something failed
        if we /0 this test will pass beacuse the function correctly raises the value error

        self.assertRaises(ValueError, calc.divide, 10, 0)
        AN ALTERNATIVE to ^^:
        with self.assertRaises(ValueError):
            calc.divide(10, 0) """


if __name__ == "__main__":
    unittest.main()
