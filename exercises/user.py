"""A class to represent a user."""


class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.status = "active"
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user."""
        print(f"{self.first_name.title()} {self.last_name.title()} is a user on our platform and is currently {self.status}.")

    def greet_user(self):
        """Display a personalised greeting to the user."""
        fullname = f"{self.first_name} {self.last_name}"
        print(f"Welcome back {fullname.title()}!")

    def increment_login_attempts(self):
        """Increment the amount of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the amount of login attempts back to 0."""
        self.login_attempts = 0
