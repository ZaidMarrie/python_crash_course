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
