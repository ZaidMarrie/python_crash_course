from user import User


class Privileges:
    """An attempt to model privileges for a user."""

    def __init__(self):
        """Initialize the privileges attributes."""
        self.privileges = ["can add post", "can remove post", "can ban user"]

    def show_privileges(self):
        """Display all the privileges this user has."""
        print("\nThis user has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Administrator(User):
    """Represent a user, with special privileges."""

    def __init__(self, first_name, last_name):
        """
        Initialize the parent attributes.
        Then initialize attributes specific to the child class.
        """
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


admin = Administrator("zaid", "marrie")
admin.privileges.show_privileges()
