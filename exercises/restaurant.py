"""A class used to represent a restaurant."""


class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Displays a short description of the restaurant."""
        print(
            f"This restaurant is called {self.restaurant_name} and serves {self.cuisine_type} cuisines.")

    def open_restaurant(self):
        """Displays a message saying that the restaurant is open."""
        print(f"{self.restaurant_name.title()} is now open!")

    def set_number_served(self, amount_served):
        """Set the number of people served to the given value."""
        if amount_served >= self.number_served:
            self.number_served = amount_served
        else:
            print("You can't roll back the number of people served.")

    def increment_number_served(self, amount):
        """Increment the number of people served by the given amount."""
        self.number_served += amount
