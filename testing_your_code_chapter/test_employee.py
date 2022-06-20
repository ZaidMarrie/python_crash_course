import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""

    def setUp(self) -> None:
        """
        Create an Employee instance
        """
        self.my_employee = Employee("bob", "willis", 35_000)

    def test_give_default_raise(self):
        """
        Test if annual_salary is raised correctly by default amount.
        """
        self.my_employee.give_raise()
        self.assertEqual(40_000, self.my_employee.annual_salary)

    def test_give_custom_raise(self):
        """
        Test if annual_salary is raised correctly by the given amount.
        """
        self.my_employee.give_raise(3_000)
        self.assertEqual(38_000, self.my_employee.annual_salary)


if __name__ == "__main__":
    unittest.main()
