# 7.1 Rental car
rental_car = input("\nWhat kind of car would you like to rent?")
print(f"\nLet me see if I can find you a {rental_car}.")

# # 7.2 Restaurant seating
group_size = input("\nHow many people are in your dinner group? ")
group_size = int(group_size)

if group_size > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("We have a table ready for you!")

# 7.3 Multiples of ten
number = input("\nTell me a number and I will tell you "
               "if its a mulple of 10 or not: ")
number = int(number)

if 10 % number == 0:
    print(f"The number {number} is a multiple of 10.")
else:
    print(f"The number {number} is Not a multiple of 10.")

# 7.4 Pizza toppings
prompt = "\nPlease tell me what topping you would like on your pizza:"
prompt += "\n(Enter 'quit' when you're finished.) "

active = True
requested_toppings = []

while active:
    requested_topping = input(prompt)

    if requested_topping == "quit":
        active = False
    else:
        print(f"\tAdding {requested_topping}...")
        requested_toppings.append(requested_topping)

print("\nYour pizza is ready!")
if requested_toppings:
    print("Your pizza has the following toppings:")
    for topping in requested_toppings:
        print("\t" + topping)

# 7.5 Movie tickets
prompt = "\nPlease tell how old you are:"
prompt += "\n(Enter 'quit' when you're finished.) "

active = True

while active:
    age = int(input(prompt))

    if age == "quit":
        active = False

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket will cost $10.")
    elif age > 12:
        print("Your ticket will cost $15.")

# 7.6 Three exits
prompt = "\nPlease tell me what topping you would like on your pizza:"
prompt += "\n(Enter 'quit' when you're finished.) "

active = True
requested_toppings = []

while active:
    requested_topping = input(prompt)

    if requested_topping == "quit":
        break
    if len(requested_toppings) >= 10:
        active = False
        print("We can only allow a maximum of 10 toppings per pizza.")

    print(f"\nAdding {requested_topping}...")
    requested_toppings.append(requested_topping)

print("\nYour pizza is ready!")
if requested_toppings:
    print("Your pizza has the following toppings:")
    for topping in requested_toppings:
        print("\t" + topping)

# 7.7 Infinity
#! The following code runs forever
# while True:
#     requested_topping = input(prompt)
#     print(f"\nAdding {requested_topping}...")

# 7.8 Deli
sandwich_orders = ["cheese", "pastrami", "chicken"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"\nMaking {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich)

# 7.9 No pastrami
sandwich_orders = ["cheese", "pastrami",
                   "chicken", "pastrami", "beef", "pastrami"]
print("\nWe have ran out of pastrami.")
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    if current_sandwich == "pastrami":
        sandwich_orders.remove("pastrami")
        continue
    else:
        print(f"\nMaking a {current_sandwich} sandwich.")

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich)

# 7.10 Dream Vacation
polling_active = True
dream_vacations = {}

while polling_active:
    name = input("\nWhat is your name? ")
    place = input(
        "If you could visit one place in the world, where would you go? ")

    dream_vacations[name] = place

    repeat = input("\nWould you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, place in dream_vacations.items():
    print(f"\t{name.title()} would like to visit {place.title()}.")
