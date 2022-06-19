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


# 10.6

# 10.7

# 10.8

# 10.9

# 10.10

# 10.11

# 10.12

# 10.13
