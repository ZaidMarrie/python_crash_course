# The input() function
message = input("Tell me something and I will repeat it back to you: ")
print(message)

# Writing clear prompts
name = input("Please enter your name: ")
print(f"\nHello, {name}")

prompt = input(
    "If you tell us who you are, we can personalize the messages you see.")
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# Using int() to accept numerical input
age = input("How old are you? ")
print(age, type(age))

age = input("How old are you? ")
age = int(age)
print(age, type(age))

height = input("How tall are you in inches? ")
height = int(height)

if height >= 48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you a little older.")

# The modulo operator
number = input("\nTell me a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

# The while loop in action
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Let the user choose when to quit
prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)

# Using a flag
prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)

# Using break to exit a loop
prompt = "\nPlease enter the name of a city that you have visited:"
prompt += "\n(Enter 'quit' when you're finished.)"

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# Using continue in a loop
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Avoiding infinite loops
x = 1
while x <= 5:
    print(x)
    x += 1

#! This loop runs forever
x = 1
while x <= 5:
    print(x)

# Moving items from one list to another
unconfirmed_users = ["alice", "brian", "candice"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"\nVerifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print("\t" + user.title())

# Removing all instances of specific values from a list
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)

# Filling a dictionary with user input
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")
