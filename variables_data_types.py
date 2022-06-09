# Variables
message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

# Naming and using variables
"""
- Variable names can only contain letters, numbers, and underscores.
- Variables can start with a letter or underscore, but not a number.
- Spaces are not allowed.
"""

# Strings
my_string_0 = "I am a string."
my_string_1 = 'I am also a string.'

# Changing Case in a String with Methods
name = "ada lovelace"
print(name.title())
print(name.upper())

name = "aDa loVelaCe"
print(name.lower())

# Using Variables in Strings
first_name = "ada"
last_name = "lovelace"
fullname = f"{first_name} {last_name}"
message = f"Hello, {fullname.title()}!"
print(message)

fullname = "{} {}".format(first_name, last_name)
print(fullname)

# Adding Whitespace to Strings with Tabs or Newlines
print("Python")
print("\tPython")

print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping Whitespace
favorite_language = "python "
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)

favorite_language = " python "
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

# Numbers
# Intergers
num1 = 5
num2 = 2
print(num1, type(num1))

result = num1 + num2
print(result)

result = num1 - num2
print(result)

result = num1 * num2
print(result)

result = num1 / num2
print(result)

three_squared = 3**2
print(three_squared)

three_cubed = 3**3
print(three_cubed)

# Floats
float_1 = 0.1
float_2 = 0.2
print(float_1, type(float_1))

# Underscores in Numbers
universal_age = 14_000_000_000
print(universal_age)

# Multiple Assignment
x, y, z = 24, 25, 26
print(x)
print(y)
print(z)

# Constants - (varible_names = all caps)
MAX_CONNECTIONS = 5000
