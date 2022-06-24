import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=5)

# Set the title and label axes.
ax.set_title("Cube Values", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cube of Values", fontsize=14)

# Set tick params
ax.tick_params(axis="both", labelsize=14)

plt.show()
