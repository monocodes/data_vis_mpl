import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(
    x_values, y_values, s=10)

# set chart title and label axes
ax.set_title('Cube Numbers', fontsize=20)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=9)

# prevent scientific notation (1_000_000 instead of 1e6)
plt.ticklabel_format(style='plain')

# set the range for each axis
ax.axis([0, 5100, 0, 130_000_000_000])

plt.show()