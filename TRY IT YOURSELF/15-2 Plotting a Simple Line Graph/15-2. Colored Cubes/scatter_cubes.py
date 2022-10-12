import matplotlib.pyplot as plt

x_values = list(range(5001))
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(
    x_values, y_values, c=y_values,
    cmap=plt.cm.spring, s=10)

# set chart title and label axes
ax.set_title('Cubes', fontsize=20)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', labelsize=9)

# prevent scientific notation (1_000_000 instead of 1e6)
plt.ticklabel_format(style='plain')

# set the range for each axis
ax.axis([0, 5100, 0, 5100**3])

plt.show()