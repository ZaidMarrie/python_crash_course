# Looping Through an Entire List
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(magician)

# Doing More Work Within a for Loop
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Doing Something After a for Loop
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

# Using the range() Function
for value in range(1, 6):
    print(value)

# Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []

for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

# Simple Statistics with a List of Numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbers_min = min(numbers)
numbers_max = max(numbers)
numbers_sum = sum(numbers)

print(numbers_min)
print(numbers_max)
print(numbers_sum)

# List Comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)

# Slicing a List
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

print(players[1:4])
print(players[:4])

print(players[2:])
print(players[-3:])

# Looping Through a Slice
players = ["charles", "martina", "michael", "florence", "eli"]

print("Here are the first 3 players on my team:")
for player in players[:3]:
    print(f"\t{player.title()}")

# Copying a List
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Tuples
# Defining a Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 # 'tuple' does not support item assignment

# Looping Through All Values in a Tuple
dimensions = (200, 50)

for dimension in dimensions:
    print(dimension)

# Writing over a Tuple
dimensions = (200, 50)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = [400, 100]
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
