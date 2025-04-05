import math


def in_table(dimensions=[100, 100], postion_vector=[50, 50]):
    if postion_vector[0] >= 0 and postion_vector[0] <= dimensions[0] and postion_vector[1] >= 0 and postion_vector[1] <= dimensions[1]:
        return True


def get_direction(position, velocity, dimensions):
    x = position[0]
    y = position[1]
    x_max = dimensions[0]
    y_max = dimensions[1]
    x_vel = velocity[0]
    y_vel = velocity[1]
    outside_wall_position = [position[0] + velocity[0], position[1] + velocity[1]]

    # LEFT WALL
    if x <= 0 and y <= y_max:
        if y_vel < 0:
            return "anti"
        else:
            return "clock"

    # TOP WALL
    if y >= y_max and x <= x_max:
        if x_vel < 0:
            return "anti"
        else:
            return "clock"

    # RIGHT WALL
    if x >= x_max and y <= y_max:
        if y_vel < 0:
            return "clock"
        else:
            return "anti"

    # BOT WALL
    if y <= 0 and x <= x_max:
        if x_vel < 0:
            return "clock"
        else:
            return "anti"


class Ball:
    def __init__(self, position_vector, velocity_vector):
        self.position_vector = position_vector
        self.velocity_vector = velocity_vector

    def get_velocity(self):
        return self.velocity_vector

    # def get_direction(self, ):
    #     pass

    def get_position(self):
        return self.position_vector

    def bounce(self, rotate_direction):

        # for 90 degrees bounces
        if rotate_direction == "clock":
            # print(self.velocity_vector)
            self.velocity_vector = [self.velocity_vector[1], -self.velocity_vector[0]]
        if rotate_direction == "anti":
            # print(self.velocity_vector)
            self.velocity_vector = [-self.velocity_vector[1], self.velocity_vector[0]]

    def move(self):
        self.position_vector = [self.position_vector[0] +
        self.velocity_vector[0], self.position_vector[1] + self.velocity_vector[1]]


class Table:
    def __init__(self, dimensions):
        self.dimensions = dimensions


position_x = int(input("Please enter your initial x position integer: "))
position_y = int(input("Please enter your initial y position integer: "))
position = [position_x, position_y]
# print(position)
# [50, 50]  # input("")

# angle from the positive x, anti-clockwise
angle = float(input("Please enter your initial angle in angles, from the positive x anticlockwise: "))  # float(input("Enter your angle: "))

# pixels per second
velocity = float(input("Enter your velocity: "))/2
# velocity_x = float(input("Please enter your initial x velocity: "))/10
# velocity_y = float(input("Please enter your initial y velocity: "))/10
# velocity = [velocity_x, velocity_y]
# velocity = float(input("Please enter your initial vector"))  # float(input("Enter your velocity: "))


position_vector_ball1 = position
velocity_vector_ball1 = (math.cos(math.radians(angle))*velocity, math.sin(math.radians(angle))*velocity)

ball1 = Ball(position_vector_ball1, velocity_vector_ball1)
print(f"initial velocity : {ball1.get_velocity()}")

dimension = [100, 100]

points = []

t = 0
for i in range(10000):
    if in_table(dimension, ball1.get_position()):
        ball1.move()
        # print(ball1.get_position())
        points.append(ball1.get_position())
        t=0
    if not in_table(dimension, ball1.get_position()) and t == 0:
        ball1.bounce(get_direction(ball1.get_position(), ball1.get_velocity(), dimension))
        ball1.move()
        # print(ball1.get_position())
        points.append(ball1.get_position())
        t=1
    if not in_table(dimension, ball1.get_position()) and t == 1:
        ball1.move()
        # print(ball1.get_position())
        points.append(ball1.get_position())
