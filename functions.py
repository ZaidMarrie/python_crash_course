# Defining a function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")


greet_user()

# Passing information to a function
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user("zaid")

# Positional arguments
def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("hamster", "harry")

# Multiple function calls
describe_pet("hamster", "harry")
describe_pet("dog", "willie")

# Keyword arguments
def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="harry", animal_type="hamster")

# Default values
def describe_pet(pet_name, animal_type="dog"):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("willie")
describe_pet(pet_name="harry", animal_type="hamster")

# Equivalent function calls
describe_pet('willie')
describe_pet(pet_name='willie')

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# Returning a simple value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    fullname = f"{first_name} {last_name}"
    return fullname.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)

# Making an argument optional
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    fullname = f"{first_name} {middle_name} {last_name}"
    return fullname.title()


musician = get_formatted_name("john", "lee", "hooker")
print(musician)


def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        fullname = f"{first_name} {middle_name} {last_name}"
    else:
        fullname = f"{first_name} {last_name}"
    return fullname.title()


musician = get_formatted_name("john", "hooker", "lee")
print(musician)

# Returning a dictionary
def build_person(first_name, last_name):
    """Return a dictionary with information about a person."""
    person = {"first_name": first_name, "last_name": last_name}
    return person


musician = build_person("jimi", "hendrix")
print(musician)


def build_person(first_name, last_name, age=None):
    """Return a dictionary with information about a person."""
    person = {"first_name": first_name, "last_name": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("jimi", "hendrix", age=27)
print(musician)

# Using a function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a fullname, neatly formatted."""
    fullname = f"{first_name} {last_name}"
    return fullname.title()


while True:
    print("\nPlease tell me your name: ")
    print("(Enter 'q' at any time to quit.)")

    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# Passing a list
def greet_users(names):
    """Display a simple greeting to each user in the list."""
    for name in names:
        print(f"\nHello, {name.title()}!")


usernames = ["hannah", "ty", "margot"]
greet_users(usernames)

# Modifying a list in a function
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()

    print(f"\nPrinting model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for model in completed_models:
    print(model)


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"\nPrinting design: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all models that were printed."""
    print("\nThe following models were printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a function from modifying a list
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs[:], completed_models)
print(unprinted_designs)

