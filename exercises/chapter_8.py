# 8.1 Message
def display_message():
    """Displays a message about what I am currently learning."""
    print("I am learning about Python's functions and how to use them.")


display_message()

# 8.2 Favorite book


def favorite_book(title):
    """Displays the users favorite book."""
    print(f"\nOne of my favorite books is '{title}'.")


favorite_book("eloquent javascript")

# 8.3 T-shirt


def make_shirt(size, message):
    """Displays the size of a shirt and the message printed on it."""
    print(
        f"\nA {size}-sized shirt was made with the message '{message}' printed on it.")


make_shirt("medium", "I love Python")
make_shirt(size="small", message="I love Python")

# 8.4 Large shirts


def make_shirt(size="large", message="I love Python"):
    """Displays the size of a shirt and the message printed on it."""
    print(
        f"\nA {size}-sized shirt was made with the message '{message}' printed on it.")


make_shirt()
make_shirt("medium")
make_shirt("small", "Python is a very powerful language")

# 8.5 Cities


def describe_city(city, country="south africa"):
    """Displays information about a city."""
    print(f"\n{city.title()} is in {country.title()}.")


describe_city("johannesburg")
describe_city("oslo", "norway")
describe_city("paris", "france")
describe_city("berlin", "germany")

# 8.6 City names


def city_country(city, country):
    """Displays a city and its country."""
    return f"{city.title()}, {country.title()}"


santiago = city_country("santiago", "chile")
print(santiago)
paris = city_country("paris", "france")
print(paris)
sydney = city_country("sydney", "australia")
print(sydney)

# 8.7 Album


def make_album(artist_name, album_name, number_of_songs=None):
    """Returns a dictionary with information about a album."""
    album = {"artist_name": artist_name, "album_name": album_name}
    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    return album


honestly_nevermind = make_album("drake", "honestly, nevermind")
print(honestly_nevermind)
vinyl_days = make_album("logic", "vinyl days")
print(vinyl_days)
honeymoon_suite = make_album("harkin", "honeymoon suite")
print(honeymoon_suite)
maelstrom = make_album("melts", "maelstrom", 8)
print(maelstrom)

# 8.8 User albums
while True:
    print("\nPlease tell me about the album")
    print("(Enter 'q' at any time to quit.)")

    artist_name = input("\nArtist name: ")
    if artist_name == "q":
        break

    album_name = input("Album name: ")
    if album_name == "q":
        break

    album = make_album(artist_name, album_name)
    print(album)

# 8.9 Messages
messages = ["hey, there!", "how are you?", "where are you?"]


def show_messages(messages):
    """Displays each message."""
    for message in messages:
        print(message)


show_messages(messages)

# 8.10 Sending sessages


def send_messages(unsent_messages, sent_messages):
    """Move each unsent message to sent_messages until none are left."""
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"\nSending message: {current_message}")
        sent_messages.append(current_message)


messages = ["hey, there!", "how are you?", "where are you?"]
sent_messages = []

send_messages(messages, sent_messages)
print(messages)
print(sent_messages)

# 8.11 Archived messages
messages = ["hey, there!", "how are you?", "where are you?"]
sent_messages = []

send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)

# 8.12 Sandwiches


def make_sandwich(*sandwich_items):
    """Summarize the sandwich being ordered."""
    print("\nYou ordered a sandwich with the following ingredients:")
    for sandwich_item in sandwich_items:
        print("- " + sandwich_item)


make_sandwich("lettuce", "tomato", "cheese", "bacon", "egg")
make_sandwich("peanut butter", "jelly")
make_sandwich("egg", "tomato", "cheese")

# 8.13 User Profile


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


my_profile = build_profile(
    "zaid", "marrie", location="johannesburg", field="programming", age=24)

# 8.14 Cars


def build_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we kown about a car."""
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info


car = build_car(
    "subaru", "outback", color="blue", tow_package=True, year=1998)
print(car)

# 8.15 Printing models
import printing_functions

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)

# 8.16 Imports
import profiler

my_profile = profiler.build_profile(
    "zaid", "marrie", age=24, city="johannesburg")
print(my_profile)

from profiler import build_profile

my_profile = build_profile("zaid", "marrie", age=24, city="johannesburg")
print(my_profile)

from profiler import build_profile as bp

my_profile = bp("zaid", "marrie", age=24, city="johannesburg")
print(my_profile)

import profiler as prf

my_profile = prf.build_profile("zaid", "marrie", age=24, city="johannesburg")
print(my_profile)

from profiler import *

my_profile = build_profile("zaid", "marrie", age=24, city="johannesburg")
print(my_profile)
