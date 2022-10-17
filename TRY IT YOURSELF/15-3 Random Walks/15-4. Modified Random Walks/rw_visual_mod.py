### 15-4. Modified Random Walks ###
"""
In the RandomWalk class, x_step and y_step are generated from the same set of conditions. The direction is chosen randomly from the list [1, -1] and the distance from the list [0, 1, 2, 3, 4]. Modify the values in these lists to see what happens to the overall shape of your walks. Try a longer list of choices for the distance, such as 0 through 8, or remove the –1 from the x or y direction list.
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)

# Emphasize the first and last points.
ax.scatter(0, 0, c='green', edgecolors='none', s=100, zorder=2)
ax.scatter(
    rw.x_values[-1], rw.y_values[-1],
    c='red', edgecolors='none', s=100)

plt.show()