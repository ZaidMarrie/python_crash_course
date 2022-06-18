# 9.1 Restaurant
from random import choice
from random import randint
from admin import Administrator
from restaurant import Restaurant


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


restaurant = Restaurant("pronto", "italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9.2 Three restaurants
restaurant_0 = Restaurant("robbies place", "african")
restaurant_1 = Restaurant("thava", "indian")
restaurant_2 = Restaurant("mozambik", "portuguese")

restaurant_0.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()

# 9.3 Users


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


user_0 = User("john", "doe")
user_0.describe_user()
user_0.greet_user()

user_1 = User("sarah", "willis")
user_1.describe_user()
user_1.greet_user()

user_2 = User("cloe", "brown")
user_2.describe_user()
user_2.greet_user()

# 9.4 Number served
restaurant = Restaurant("pronto", "italian")
print(restaurant.number_served)
restaurant.number_served = 7
print(restaurant.number_served)

restaurant.set_number_served(20)
print(restaurant.number_served)

restaurant.increment_number_served(5)
print(restaurant.number_served)

# 9.5 Login attempts
my_user = User("zaid", "marrie")

my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
print("Login attempts:", my_user.login_attempts)

my_user.reset_login_attempts()
print("Login attempts:", my_user.login_attempts)

# 9.6 Ice cream stand


class IceCreamStand(Restaurant):
    """Represent a restaurant, specific to ice cream stands."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize the parent attributes.
        Then initialize attributes specific to the child class.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "bubblegum"]

    def display_flavors(self):
        """Display the list of flavors."""
        print("\nThe following flavors are sold here:")
        for flavor in self.flavors:
            print(f"- {flavor} flavor")


my_icecream_stand = IceCreamStand("frosty scoops", "ice cream")
my_icecream_stand.display_flavors()

# 9.7 Admin


class Administrator(User):
    """Represent a user, with special privileges."""

    def __init__(self, first_name, last_name):
        """
        Initialize the parent attributes.
        Then initialize attributes specific to the child class.
        """
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can remove post", "can ban user"]

    def show_privileges(self):
        """Display all the privileges this user has."""
        print("\nThis user has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Administrator("zaid", "marrie")
admin.show_privileges()

# 9.8 Privileges


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

# 9.9 Battery upgrade


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery capacity to 100."""
        if self.battery_size != 100:
            self.battery_size = 100
        else:
            print("This battery cannot be upgraded any further.")


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the cars mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attemps to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.
        Then initialize attributes specifice to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar("tesla", "model s", 2019)
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

# 9.10 Imported restaurant

my_restaurant = Restaurant("zaids place", "exotic")
my_restaurant.describe_restaurant()
my_restaurant.increment_number_served(1)
my_restaurant.increment_number_served(4)
my_restaurant.increment_number_served(8)
print(my_restaurant.number_served)

# 9.11 Imported admin

admin = Administrator("zaid", "marrie")
admin.privileges.show_privileges()

# 9.12 Multiple Modules
# * This exercise was completed in another file("admin.py")

# 9.13 Dice


class Die:
    """A simple attempt to model a die."""

    def __init__(self, sides=6):
        """Initialize the die attributes."""
        self.sides = sides

    def roll_die(self):
        """
        Prints a random number between 1 and the number of sides on the die.
        """
        print(randint(1, self.sides))


six_sided_die = Die()
for i in range(11):
    six_sided_die.roll_die()

ten_sided_die = Die(10)
for i in range(11):
    ten_sided_die.roll_die()

twenty_sided_die = Die(20)
for i in range(11):
    twenty_sided_die.roll_die()

# 9.14 Lottery

lottery_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c" "d", "e"]
winning_choices = []

while len(winning_choices) < 5:
    current_pick = choice(lottery_choices)
    if current_pick not in winning_choices:
        winning_choices.append(current_pick)

print("\nAny ticket matching this sequence of numbers/letters wins the grand prize.")
print(winning_choices)

# 9.15 Lottery Analysis
lottery_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e"]
drawing_tickets = True
iterations = 0

while drawing_tickets:
    my_ticket = []
    amount_correct = 0

    for i in range(5):
        current_pick = choice(lottery_choices)
        if current_pick not in my_ticket:
            my_ticket.append(current_pick)

    for pick in my_ticket:
        if pick in winning_choices:
            amount_correct += 1
        else:
            break

    print(my_ticket, winning_choices, f"Iteration: {iterations}")
    iterations += 1

    if amount_correct == 5:
        print("\nWinning ticket found!")
        drawing_tickets = False

print(my_ticket, "  |  ", winning_choices, f"\nIteration: {iterations}")
