import math


def in_table(dimensions=[100, 100, 100], postion_vector=[50, 50, 50]):
    if postion_vector[0] >= 0 and postion_vector[0] <= dimensions[0] and postion_vector[1] >= 0 and postion_vector[1] <= dimensions[1] and postion_vector[2] >= 0 and postion_vector[2] <= dimensions[2]:
        return True



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

    def bounce(self, position, velocity, dimensions):
        x = position[0]
        y = position[1]
        z = position[2]
        x_max = dimensions[0]
        y_max = dimensions[1]
        z_max = dimensions[2]
        x_vel = velocity[0]
        y_vel = velocity[1]
        z_vel = velocity[2]
        # ??????? outside_wall_position = [position[0] + velocity[0], position[1] + velocity[1], position[2] + velocity[2]]

        # LEFT WALL
        if x <= 0 and (0<=y<=y_max) and (0<=z<=x_max):
            self.velocity_vector[0] *= -1

        # FRONT
        if (0<=x<=x_max) and (0<=y<=y_max) and z<=0:
            self.velocity_vector[2] *= -1

        # BOTTOM
        if (0<=x<=x_max) and (0<=z<=z_max) and y<=0:
            self.velocity_vector[1] *= -1

        # TOP
        if (0<=x<=x_max) and (0<=z<=z_max) and y>=y_max:
            self.velocity_vector[1] *= -1

        # BACK
        if (0<=x<=x_max) and (0<=y<=y_max) and z>=z_max:
            self.velocity_vector[2] *= -1

        # RIGHT
        if (0<=z<=z_max) and (0<=y<=y_max) and x>=x_max:
            self.velocity_vector[0] *= -1

    def move(self):
        self.position_vector = [self.position_vector[0] +
        self.velocity_vector[0], self.position_vector[1] + self.velocity_vector[1], self.position_vector[2] + self.velocity_vector[2]]


class Table:
    def __init__(self, dimensions):
        self.dimensions = dimensions


position_x = int(input("Please enter your initial x position integer: "))
position_y = int(input("Please enter your initial y position integer: "))
position_z = int(input("Please enter your initial z position integer: "))

position = [position_x, position_y, position_z]
# print(position)
# [50, 50]  # input("")

# angle from the positive x, anti-clockwise
angle = float(input("Please enter your initial angle in angles, from the positive x anticlockwise: "))
theta = float(input("Please enter your initial angle in angles, from the positive x anticlockwise into depth: "))

# float(input("Enter your angle: "))

# pixels per second
velocity = float(input("Enter your velocity: "))/2
# velocity_x = float(input("Please enter your initial x velocity: "))/10
# velocity_y = float(input("Please enter your initial y velocity: "))/10
# velocity = [velocity_x, velocity_y]
# velocity = float(input("Please enter your initial vector"))  # float(input("Enter your velocity: "))


position_vector_ball1 = position
x = velocity * math.sin(theta) * math.cos(angle)
y = velocity * math.sin(theta) * math.sin(angle)
z = velocity * math.cos(theta)
velocity_vector_ball1 = [x, y, z]

ball1 = Ball(position_vector_ball1, velocity_vector_ball1)
print(f"initial velocity : {ball1.get_velocity()}")

dimension = [100, 100, 100]

points = []

t = 0
for i in range(1000):
    if in_table(dimension, ball1.get_position()):
        ball1.move()
        # print(ball1.get_position())
        points.append(ball1.get_position())
        t=0
    if not in_table(dimension, ball1.get_position()) and t == 0:
        # print("AFUHQIUEHFGIUHWGEAFGUYIH")
        ball1.bounce(ball1.get_position(), ball1.get_velocity(), dimension)
        ball1.move()
        # print(ball1.get_position())
        points.append(ball1.get_position())
        t=1
    if not in_table(dimension, ball1.get_position()) and t == 1:
        ball1.move()
        # print(ball1.get_position())
        points.append(ball1.get_position())
# print(points)
