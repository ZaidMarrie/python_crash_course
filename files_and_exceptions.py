# Reading from a file
# Reading an entire file
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
