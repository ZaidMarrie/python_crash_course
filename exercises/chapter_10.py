# 10.1 Learning python
filename = "learning_python.txt"

with open(filename) as file_object:
    content = file_object.read()
print("\n", content.rstrip())

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

# 10.2 Learning C
filename = "learning_python.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace("Python", "JavaScript")
    print("\n", line)

# 10.3 Guest
filename = "guest.txt"

with open(filename, "w") as file_object:
    guest = input("What is your name? ")
    file_object.write(guest)

# 10.4 Guest Book
filename = "guest_book.txt"
polling_active = True

while polling_active:
    prompt = "\nPlease tell me what your name is: "
    prompt += "(Enter 'q' anytime to quit.)"

    name = input(prompt)
    if name == "q":
        polling_active = False
    else:
        print(f"\nWelcome, {name.title()}")
        with open(filename, "a") as file_object:
            visit_message = f"{name.title()} has visited.\n"
            file_object.write(visit_message)


# 10.5 Programming poll
filename = "programming_poll.txt"
polling_active = True

while polling_active:
    prompt = "\nPlease tell me why you like programming: "
    prompt += "(Enter q anytime to quit.)"

    reason = input(prompt)
    if reason == "q":
        polling_active = False
    else:
        with open(filename, "a") as file_object:
            file_object.write(reason + "\n")


# 10.6 Addition
print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")
try:
    first_number = int(input("First number: "))
    second_number = int(input("Second number: "))
except ValueError:
    print("You can only add numbers!")
else:
    print(first_number + second_number)

# 10.7 Addition calculator
print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("First number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break

    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        print("You can only add numbers!")
    else:
        print(first_number + second_number)

# 10.8 Cats and dogs
filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist")

# 10.9 Silent cats and dogs
filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        pass

# 10.10 Common words
filename = "american_notes.txt"


def count_word_presence(file, word="the"):
    """Counts how many times the specified word appears in a text file."""
    try:
        with open(file, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("The file does not exist!")
    else:
        word_count = 0
        for line in lines:
            line = line.lower()
            word_count += line.count(word)
        print(f"The word '{word}' appears {word_count} times in the text.")


count_word_presence(filename)
count_word_presence(filename, "the ")

# 10.11 Favorite number

# 10.12 Favorite number remembered


# 10.13 Verify user
