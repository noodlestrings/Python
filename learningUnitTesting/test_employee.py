import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('\ntearDownClass')

    def setUp(self):  # runs before every test
        self.emp1 = Employee("John", "Stamos", 45000)
        self.emp2 = Employee("Anthony", "Cumea", 99000)

    def tearDown(self):  # runs after every test
        pass

    def test_email(self):

        self.assertEqual(self.emp1.email, "John.Stamos@email.com")
        self.assertEqual(self.emp2.email, "Anthony.Cumea@email.com")

        self.emp1.first = "Vladimir"
        self.emp2.last = "Joshua"
        self.assertEqual(self.emp1.email, "Vladimir.Stamos@email.com")
        self.assertEqual(self.emp2.email, "Anthony.Joshua@email.com")

    def test_fullname(self):

        self.assertEqual(self.emp1.fullname, "John Stamos")
        self.assertEqual(self.emp2.fullname, "Anthony Cumea")

        self.emp1.first = "avery"
        self.emp2.last = "hopkins"
        self.assertEqual(self.emp1.fullname, "avery Stamos")
        self.assertEqual(self.emp2.fullname, "Anthony hopkins")

    def test_apply_raise(self):

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 47250)
        self.assertEqual(self.emp2.pay, 103950)

        self.emp2.pay = 101000
        self.emp2.apply_raise()
        self.assertEqual(self.emp2.pay, 101000*1.05)


if __name__ == "__main__":
    unittest.main()
