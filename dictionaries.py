# A simple dictionary
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

# Accessing values in a dictionary
alien_0 = {"color": "green"}
print(alien_0["color"])

alien_0 = {"color": "green", "points": 5}
new_points = alien_0["points"]
print(f"You've just earned {new_points} points.")

# Adding new key-value pairs
alien_0 = {"color": "green", "points": 5}
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# Starting with an empty dictionary
alien_0 = {}

alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

# Modifying values in a dictionary
alien_0 = {"color": "green"}
print(f"The alien is {alien_0['color']}.")

alien_0["color"] = "yellow"
print(f"The alien is now {alien_0['color']}.")

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0['x_position']}")

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New position: {alien_0['x_position']}.")

# Removing key-value pairs
alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"]
print(alien_0)

# A dictionary of similar objects
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")

# Using get() to access values
alien_0 = {"color": "green", "speed": "slow"}

point_value = alien_0.get("points", "No point value assigned.")
print(point_value)

# Looping through all key-value pairs
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi"
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping through all the keys in a dictionary
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

for name in favorite_languages.keys():
    print(name.title())

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if "erin" not in favorite_languages.key():
    print("Erin, please take our poll!")

# Looping through a dictionaries key in a particular order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking our poll.")

# Looping through all values in a dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())

