# Reading from a file
# Reading an entire file
import json
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
print(contents)
print(contents.rstrip())

# Reading line by line
filename = "pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

# Making a list of lines from a file
filename = "pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

# Working with a files contents
filename = "pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# Large files: one million digits
filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# Is your birthday contained in Pi?
birthday = input("Enter your birthday, in the form of mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of Pi.")
else:
    print("Your birthday does not appear in the first million digits of Pi.")

# Writing to a file
# Writing to an empty file
filename = "programming.txt"

with open(filename, "w") as file_object:
    file_object.write("I love programming.")

# Writing multiple lines
filename = "programming.txt"

with open(filename, "w") as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# Appending to a file
filename = "programming.txt"

with open(filename, "a") as file_object:
    file_object.write("I also love finding meaning in large data sets.\n")
    file_object.write("I love creating apps that can run in the browser.\n")

# Exceptions
# Handling the ZeroDivisionError exception
# print(5/0) #! I raise an exception

# Using try-except blocks
try:
    print(5/0)
except ZeroDivisionError:
    print("\nYou can't divide by 0.")

# Using exceptions to prevent crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("\nSecond number: ")
    if second_number == "q":
        break
    answer = int(first_number) / int(second_number)
    print(answer)

# The else block
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("\nSecond number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# Handling the FileNotFoundError exception
filename = "alice.txt"
try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file '{filename}' does not exist.")

# Analyzing text
filename = "alice.txt"
try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file '{filename}' does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file '{filename}' has about {num_words} words.")

# Working with multiple files


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file '{filename}' has about {num_words} words.")


filename = "alice.txt"
count_words(filename)

filenames = ["alice.txt", "siddhartha.txt",
             "moby_dick.txt", "little_women.txt"]
for filename in filenames:
    count_words(filename)

# Failing silently


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file '{filename}' has about {num_words} words.")


filenames = ["alice.txt", "siddhartha.txt",
             "moby_dick.txt", "little_women.txt"]
for filename in filenames:
    count_words(filename)

# Storing data
# Using json.dump() and json.load()

filename = "numbers.json"
numbers = [2, 3, 5, 7, 11, 13]

with open(filename, "w") as f:
    json.dump(numbers, f)

with open(filename) as f:
    numbers = json.load(f)

print(numbers)

# Saving and using user-generated data
filename = "username.json"
username = input("What is your name? ")

with open(filename, "w") as f:
    json.dump(username, f)
    print(f"We'll remember you come back, {username}!")

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")


try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, "w") as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")

# Refactoring


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
