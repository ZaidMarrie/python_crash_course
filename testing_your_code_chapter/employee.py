class Employee:
    """A simple attempt to model an employee."""

    def __init__(self, first, last, annual_salary):
        """Initialize employee attributes."""
        self.first = first
        self.last = last
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5_000):
        """Increment annual_salary by 5000 if amount not given."""
        self.annual_salary += raise_amount
