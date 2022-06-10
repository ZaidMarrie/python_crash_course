# A Simple List
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# Accessing Elements in a List
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles[0])

print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])

print(bicycles[-1])  # Gets last element

# Using Individual Values from a List
bicycles = ["trek", "cannondale", "redline", "specialized"]
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# Modifying Elements in a List
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

# Appending Elements to the End of a List
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles = []

motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")

print(motorcycles)

# Inserting Elements into a List at a Specified Index
motorcycles = ["honda", "yamaha", "suzuki"]

motorcycles.insert(0, "ducati")
print(motorcycles)

# Removing an Item Using the 'del' Statement
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

popped_motorcycle = motorcycles.pop()  # Pops off last item
print(motorcycles)
print(popped_motorcycle)

motorcycles = ["honda", "yamaha", "suzuki"]
last_owned_motorcycle = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned_motorcycle.title()}.")

# Popping Items from any Position in a List
motorcycles = ["honda", "yamaha", "suzuki"]

first_owned_motorcycle = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned_motorcycle.title()}.")

# Removing an Item by Value
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

motorcycles.remove("ducati")
print(motorcycles)

# Sorting a List Permanently with the sort() Method
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

# Sorting a List Permanently with the sort() Method in Reverse Alphabetical Order
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
cars = ["bmw", "audi", "toyota", "subaru"]

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Printing a List in Reverse Order
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

cars.reverse()
print(cars)

# Finding the Length of a List
cars = ["bmw", "audi", "toyota", "subaru"]
cars_length = len(cars)
print(cars_length)

# Avoiding Index Errors When Working with Lists
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3]) # Raises IndexError
