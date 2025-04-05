import twod_ninety_degree_bounce_data
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


xs = []
ys = []


for point in twod_ninety_degree_bounce_data.points:
    xs.append(point[0])
    ys.append(point[1])


fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
line, = ax.plot([], [], 'b-',animated=True, lw=2)  # blue line
dot, = ax.plot([], [], 'ro', animated=True)         # red dot at the head


def init():
    line.set_data([], [])
    dot.set_data([], [])
    return line, dot

# Update function
def update(frame):
    line.set_data(xs[:frame], ys[:frame])  # draw path
    dot.set_data([xs[frame]], [ys[frame]])  # current position
    return line, dot


ani = FuncAnimation(fig, update, frames=len(xs), init_func=init,
                interval=1, blit=True)

plt.gca().set_aspect('equal')
plt.show()
