# 6.1 Person
person_0 = {"first_name": "zaid", "last_name": "marrie",
            "age": 24, "city": "johannesburg"}

print(person_0["first_name"])
print(person_0["last_name"])
print(person_0["age"])
print(person_0["city"])

# 6.2 Favorite numbers
favorite_numbers = {
    "jen": 88,
    "stowie": 25,
    "kevin": 12,
    "miley": 11,
    "walie": 7
}
print(favorite_numbers["jen"])
print(favorite_numbers["stowie"])
print(favorite_numbers["kevin"])
print(favorite_numbers["miley"])
print(favorite_numbers["walie"])

# 6.3 Glossary
glossary = {
    "variables": "A variable is a label, which is used to reference a value associated with that label.",
    "lists": "A list in Python, is a collection of values that are indexed, changeable, ordered, and can contain duplicates.",
    "dictionaries": "A dictionary in Python, is a collection of key-value pairs which stores related data.",
    "loop": "A loop is a set of instructions that are repeated over and over until a certain condition evaluates to false.",
    "conditionals": "A conditional is an expression that evaluates to True/False."
}

print("\nVariables:", glossary["variables"])
print("\nLists:", glossary["lists"])
print("\nDictionaries:", glossary["dictionaries"])
print("\nLoop:", glossary["loop"])
print("\nConditional:", glossary["conditionals"])

# 6.4 Glossary 2
glossary["argument"] = "An argument is a way to provide information to a function."
glossary["assignment operator"] = "An assignment operator is used to assign a value to a variable."
glossary["program"] = "A program is an organized set of instructions, that performs a task when executed."
glossary["boolean"] = "A boolean is a type of value that can be either True/False."
glossary["constant"] = "A constant is a value that does not change throughout a programs life cycle."

for term, desc in glossary.items():
    print(f"{term.title()}: ", desc)

# 6.5 Rivers
rivers = {"nile": "egypt", "vaal": "south africa", "zembezi": "zambia"}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("The following rivers were mentioned:")
for river in rivers.keys():
    print(f"\t{river.title()}")

print("The following rivers were mentioned:")
for country in rivers.values():
    print(f"\t{country.title()}")

# 6.6 Polling
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}
people = ["chris", "edward", "gloria", "jen"]

for name in favorite_languages.keys():
    if name in people:
        print(f"{name.title()}, thank you for taking the poll.")
    else:
        print(f"{name.title()}, please take the poll.")

# 6.7 People
people = {
    "emerit": {
        "first_name": "eric",
        "last_name": "merit",
        "age": 37,
        "city": "valencia"
    },
    "ksavic": {
        "first_name": "kevio",
        "last_name": "savic",
        "age": 63,
        "city": "oslo"
    },
    "zmarie": {
        "first_name": "zaid",
        "last_name": "marrie",
        "age": 24,
        "city": "johannesburg"
    }
}

for person, person_info in people.items():
    print(f"\nUsername: {person}")
    fullname = f"{person_info['first_name'].title()} {person_info['last_name'].title()}"

    print(f"\tFullname: {fullname}")
    print(f"\tAge: {person_info['age']}")
    print(f"\tCity: {person_info['city']}")

# 6.8 Pets
pets = [
    {
        "animal_type": "dog",
        "owner": "will",
        "legs": 4
    },
    {
        "animal_type": "cat",
        "owner": "elizabeth",
        "legs": 4
    },
    {
        "animal_type": "bird",
        "owner": "frank",
        "legs": 2
    }
]

for pet in pets:
    print("\nThese following pets from my neighborhood:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

# 6.9 Favorite places
favorite_places = {
    "jen": ["rome", "paris"],
    "joe": ["texas", "los angeles", "san francisco"],
    "celine": ["sydney", "paris", "singapore"]
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are: ")
    for place in places:
        print(f"\t{place.title()}")

# 6.10 Favorite Numbers
favorite_numbers = {
    "jen": [88, 33, 55],
    "stowie": [25, 13, 1],
    "kevin": [12, 6],
    "miley": [11, 7],
    "walie": [7, 11, 21]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s numbers are: ")
    for number in numbers:
        print(f"\t{number}")

# 6.11 Cities
cities = {
    "sydney": {
        "country": "australia",
        "population": 5_312_000,
        "fact": "Sydney has more than 100 beaches."
    },
    "oslo": {
        "country": "norway",
        "population": 634_293,
        "fact": "The Frogner Park is the world’s largest sculpture park."
    },
    "las_vegas": {
        "country": "united states of america",
        "population": 644_594,
        "fact": "The city sees over 300 weddings a day"
    },
    "paris": {
        "country": "france",
        "population": 2_161_000,
        "fact": "Paris has one of the most famous paintings in the world."
    },
    "berlin": {
        "country": "berlin",
        "population": 3_645_000,
        "fact": "Berlin is home to the worlds longest beer garden."
    }
}

for city, city_info in cities.items():
    print(f"\nThe city of {city.title()}:")

    for key, value in city_info.items():
        print(f"\t{key.title()}: {value}")
