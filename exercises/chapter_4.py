# 4.1 Pizzas
pizzas = ["cheese", "pepperoni", "hawaiian"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("\nI like pizza very much and the following are my favorites:")

for pizza in pizzas:
    print(f"\t{pizza} pizza")

print("\nI really love pizza!")

# 4.2 Animals
animals = ["cat", "dog", "sheep"]

for animal in animals:
    print(animal)
    print(f"A {animal} would make a great pet.")

print("The pets mentioned above all have 4 legs.")

# 4.3 Counting to Twenty
for number in range(21):
    print(number)

# 4.4 One Million
one_million = list(range(1, 1_000_001))

for number in one_million:
    print(number)

# 4.5 Summing a Million
one_million = list(range(1, 1_000_001))
min_of_million = min(one_million)
max_of_million = max(one_million)
sum_of_million = sum(one_million)

print(min_of_million)
print(max_of_million)
print(sum_of_million)

# 4.6 Odd Numbers
odd_numbers = list(range(1, 21, 2))

for num in odd_numbers:
    print(num)

# 4.7 Threes
threes = list(range(3, 31, 3))

for num in threes:
    print(num)

# 4.8 Cubes
cubes = []

for value in range(1, 11):
    cube = value**3
    cubes.append(cube)

print(cubes)

# 4.9 Cube Comprehesion
cubes = [value**3 for value in range(1, 11)]
print(cubes)

# 4.10 Slices
cubes = [value**3 for value in range(1, 11)]

print("The first three numbers cubed from 1 to 10 are:")
print(cubes[:3])

print("Three numbers cubed from the middle in the range of 1-10 are:")
print(cubes[3:7])

print("The last three numbers cubed from 1 to 10 are:")
print(cubes[-3:])


# 4.11 My Pizzas, Your Pizzas
my_pizzas = ["cheese", "pepperoni", "hawaiian"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("vegetable")
friend_pizzas.append("meaty")

print("My favorite pizza's are:")
for pizza in my_pizzas:
    print(f"\t{pizza} pizza")

print("My friend's favorite pizza's are:")
for pizza in friend_pizzas:
    print(f"\t{pizza} pizza")

# 4.12 More Loops
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

for food in my_foods:
    print(food)

for food in friend_foods:
    print(food)

# 4.13 Buffet
restaurant_foods = ("pasta", "seafood", "soup", "veggies", "salad")
for food in restaurant_foods:
    print(food)

# restaurant_foods[0] = "beef" # Cannot modify tuple elements

restaurant_foods = ("pasta", "beef", "soup", "lamb", "salad")
for food in restaurant_foods:
    print(food)

# 4.14 PEP 8
# https://peps.python.org/pep-0008/
