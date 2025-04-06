import test

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Setup figure and 3D axis ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_zlim(0, 100)

xs = []
ys = []
zs = []

for point in test.points:
    xs.append(point[0])
    ys.append(point[1])
    zs.append(point[2])

# print(xs, ys, zs)

# Create the dot
dot, = ax.plot([], [], [], 'ro', markersize=6)
line, = ax.plot([], [], [], 'b-', animated=True)


def init():
    line.set_data([], [])
    line.set_3d_properties([])
    dot.set_data([], [])
    dot.set_3d_properties([])
    return dot, line


def update(frame):
    line.set_data(xs[:frame], ys[:frame])
    line.set_3d_properties(zs[:frame])
    dot.set_data([xs[frame]], [ys[frame]])  # Set x and y
    dot.set_3d_properties([zs[frame]])
    return dot, line


ani = FuncAnimation(fig, update, init_func=init,
                    frames=len(xs), interval=20, blit=False)

plt.title("3D Bouncing Dot")
plt.show()

