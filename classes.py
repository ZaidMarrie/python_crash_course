# Creating and using a class
# Creating the dog class

from car import Car, ElectricCar
from car import Car


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over.")


# Making an instance from a class
my_dog = Dog("willie", 6)

# Accessing attributes
print(f"My dogs name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Calling methods
my_dog.sit()
my_dog.roll_over()

# Creating multiple instances of a class
my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)

print(f"\nMy dogs name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dogs name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# Working with classes and instances
# The car class


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

# Setting a default value for an attribute


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


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying attribute values
# Modifying an attributes value directly
my_new_car = Car("audi", "a4", 2019)
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an attributes value through a method


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


my_new_car = Car("audi", "a4", 2019)
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# Incrementing an attributes value through a method


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


my_used_car = Car("subaru", "outback", 2015)
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# Inheritance
# The __init__() method for a child class


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of parent class."""
        super().__init__(make, model, year)


my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())

# Defining attributes and methods for the child class


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.
        Then initialize attributes specifice to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# Instances as attributes


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
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Importing classes
# Importing a single class

my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

# Importing multiple classes from a module

my_beetle = Car("volkswagen", "beetle", 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla", "roadster", 2019)
print(my_tesla.get_descriptive_name())

# The Python standard library
from random import randint
from random import choice

print(randint(1, 6))

players = ["charles", "martina", "michael", "florence", "eli"]
first_up = choice(players)
print(first_up)
