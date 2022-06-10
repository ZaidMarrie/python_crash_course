# 3.1 Names
names = ["kyle", "lisa", "sarah", "robin", "howard"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

# 3.2 Greetings
names = ["kyle", "lisa", "sarah", "robin", "howard"]
message = "Hello, {}!"
print(message.format(names[0]))
print(message.format(names[1]))
print(message.format(names[2]))
print(message.format(names[3]))
print(message.format(names[4]))

# 3.3 Your Own List
my_list = ["honda", "toyota", "subaru", "audi", "mercedes benz"]
print(f"I would like to own a {my_list[0]} car.")
print(f"I would like to own a {my_list[1]} car.")
print(f"I would like to own a {my_list[2]} car.")
print(f"I would like to own a {my_list[3]} car.")
print(f"I would like to own a {my_list[4]} car.")

# 3.4 Guest List
guest_list = ["Claude", "Phil", "Jesse"]
print(f"Hi, {guest_list[0]}, would you like to join me for dinner?")
print(f"Hi, {guest_list[1]}, would you like to join me for dinner?")
print(f"Hi, {guest_list[2]}, would you like to join me for dinner?")

# 3.5 Changing Guest List
guest_list = ["Claude", "Phil", "Jesse"]

unavailable_guest = guest_list.pop(1)
print(f"{unavailable_guest} cannot make it to dinner!")

guest_list.insert(1, "Andrea")
print(f"Hi {guest_list[0]}, are you still joining me for dinner?")
print(f"Hi {guest_list[1]}, are you still joining me for dinner?")
print(f"Hi {guest_list[2]}, are you still joining me for dinner?")

# 3.6 More Guests
guest_list = ["Claude", "Andrea", "Jesse"]
print("I just found a bigger dinner table!")

guest_list.insert(0, "Melody")
guest_list.insert(2, "Chris")
guest_list.append("Alex")

print(f"Hi {guest_list[0]}, will you join us for dinner?")
print(f"Hi {guest_list[1]}, will you join us for dinner?")
print(f"Hi {guest_list[2]}, will you join us for dinner?")
print(f"Hi {guest_list[3]}, will you join us for dinner?")
print(f"Hi {guest_list[4]}, will you join us for dinner?")
print(f"Hi {guest_list[5]}, will you join us for dinner?")

# 3.7 Shrinking Guest List
guest_list = ["Melody", "Claude", "Chris", "Andrea", "Jesse", "Alex"]
print("Oh No! The dinner table won't arrive in time, so I can only invite two people")

popped_guest = guest_list.pop()
print(f"{popped_guest}, I am so sorry that I cannot invite you to dinner.")

popped_guest = guest_list.pop()
print(f"{popped_guest}, I am so sorry that I cannot invite you to dinner.")

popped_guest = guest_list.pop()
print(f"{popped_guest}, I am so sorry that I cannot invite you to dinner.")

popped_guest = guest_list.pop()
print(f"{popped_guest}, I am so sorry that I cannot invite you to dinner.")

print(f"{guest_list[0]}, you are still invited for dinner.")
print(f"{guest_list[1]}, you are still invited for dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)

# 3.8 Seeing The World
locations = ["paris", "rome", "oslo", "sydney", "berlin"]
print(locations)

print(sorted(locations))

print(locations)

print(sorted(locations, reverse=True))

print(locations)

locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)

# 3.9 Dinner Guests
guest_list = ["Claude", "Phil", "Jesse"]
print(f"I will be inviting {len(guest_list)} people to dinner.")

unavailable_guest = guest_list.pop(1)
guest_list.insert(1, "Andrea")
print(f"I will be inviting {len(guest_list)} people to dinner.")

guest_list.insert(0, "Melody")
guest_list.insert(2, "Chris")
guest_list.append("Alex")
print(f"I will be inviting {len(guest_list)} people to dinner.")

popped_guest = guest_list.pop()
popped_guest = guest_list.pop()
popped_guest = guest_list.pop()
popped_guest = guest_list.pop()

del guest_list[0]
del guest_list[0]

print(f"I will be inviting {len(guest_list)} people to dinner.")

# 3.10 Every Function
cities = ["johannesburg", "sydney", "oslo"]
oslo = cities.pop()
cities.insert(1, "berlin")
cities.append("rome")
cities[2] = "paris"
del cities[-1]
cities.remove("johannesburg")
cities_sorted = cities.sort()
cities_sorted_reverse = cities.sort(reverse=True)
print(sorted(cities))
print(sorted(cities, reverse=True))
cities.reverse()
print(len(cities))

# 3.11 Intentional Error
cities = ["johannesburg", "sydney", "oslo"]
# print(cities[5]) # Raises IndexError
