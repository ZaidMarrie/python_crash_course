# 5.1 Conditional Tests
car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("Is car == 'audi'? I predict False.")
print(car == "audi")

print("Is car != 'audi'? I predict True.")
print(car != "audi")

print("Is car.upper() == 'Subaru'? I predict True")
print(car.upper() == "Subaru")

print("Is 5 < 3 ? I predict False.")
print(5 < 3)

print("Is 5 > 3 ? I predict True.")
print(5 > 3)

print("Is 10 >= 10 ? I predict True.")
print(10 >= 10)

print("Is 10 > 10 ? I predict False.")
print(10 > 10)

print("Is car == 'audi' or car == 'bmw'? I predict False.")
print(car == "audi" or car == "bmw")

print("Is 2 > 3 or 2 > 5 ? I predict False.")
print(2 > 3 or 2 > 5)

# 5.2 More Conditional Tests
car = "Subaru"
print(car.lower() == "subaru", "I predict True")

print(car == "subaru", "I predict False.")

# 5.3 Alien Colors #1
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points.")

alien_color = "yellow"
if alien_color == "green":
    print("You just earned 5 points.")

# 5.4 Alien Colors #2
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points.")
else:
    print("You just earned 10 points.")

alien_color = "yellow"
if alien_color == "green":
    print("You just earned 5 points.")
else:
    print("You just earned 10 points.")

# 5.5 Alien Colors #3
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points.")
elif alien_color == "yellow":
    print("You just earned 10 points.")
else:
    print("You just earned 15 points.")

alien_color = "yellow"
if alien_color == "green":
    print("You just earned 5 points.")
elif alien_color == "yellow":
    print("You just earned 10 points.")
else:
    print("You just earned 15 points.")

alien_color = "red"
if alien_color == "green":
    print("You just earned 5 points.")
elif alien_color == "yellow":
    print("You just earned 10 points.")
else:
    print("You just earned 15 points.")

# 5.6 Stages of life
age = 12

if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")

# 5.7 Favorite Fruit
favorite_fruits = ["kiwi", "apple", "banana"]

if "kiwi" in favorite_fruits:
    print("You really like kiwis!")
if "apple" in favorite_fruits:
    print("You really like apples!")
if "banana" in favorite_fruits:
    print("You really like bananas!")
if "naartjie" in favorite_fruits:
    print("You really like naartjies!")
if "pear" in favorite_fruits:
    print("You really like pears!")

# 5.8 Hello Admin
users = ["zmarrie", "jdoe", "kstance", "buster", "admin"]

for user in users:
    if user == "admin":
        print(f"Hello {user.title()}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in.")

# 5.9 No Users
users = []

if users:
    for user in users:
        if user == "admin":
            print(
                f"Hello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in.")
else:
    print("We need to find some users!")

# 5.10 Checking Usernames
current_users = ["zaid", "jane", "joe", "kyle", "hannah"]
new_users = ["jane", "jenna", "susan", "kyle", "howard"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Oops! That username has been taken. Please use another username.")
    else:
        print("Woohoo! That username is available.")

# 5.11 Ordinal Numbers
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        ordinal_ending = "st"
    elif number == 2:
        ordinal_ending = "nd"
    elif number == 3:
        ordinal_ending = "rd"
    else:
        ordinal_ending = "th"

    ordinal_number = str(number) + ordinal_ending
    print(ordinal_number)
