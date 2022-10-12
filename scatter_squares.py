import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', s=10)

# Defining Custom Colors
"""
to define custom color, pass the c argument a tuple with three decimal values between 0 and 1
For example, plot with light-green dots:
ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
"""

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])

# Prevent scientific notation (1e6 instead of 1_000_000)
plt.ticklabel_format(style='plain')

plt.show()