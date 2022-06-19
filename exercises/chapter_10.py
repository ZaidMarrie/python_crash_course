# 10.1 Learning python
filename = "learning_python.txt"

with open(filename) as file_object:
    content = file_object.read()
print(content.rstrip())

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

# 10.2 Learning C
filename = "learning_python.txt"

with open(filename) as file_object:
    for line in file_object:
        line.replace("Python", "JavaScript")
        print(line)

# 10.3

# 10.4

# 10.5

# 10.6

# 10.7

# 10.8

# 10.9

# 10.10

# 10.11

# 10.12

# 10.13
