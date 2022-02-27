import turtle as t
import random

lily = t.Turtle()
t.colormode(255)
lily.shape('turtle')
lily.speed('fastest')
lily.pensize(3)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


# project 1 - overlapping shapes
# a = 0
# b = 4
# while a < 8:
#     okay = random.choices(colors)
#     lily.color(okay)
#     for i in range(b):
#         lily.right(360/b)
#         lily.forward(100)
#     b += 1
#     a += 1

# project 2 random_walk
# c = 0
# d = [90, 270, 180, 0]
# for i in range(200):
#     lily.color(random_color())
#     e = random.choice(d)
#     lily.setheading(e)
#     lily.forward(20)

# project 3 - spirograph
# angle = 5
# f = int(360 / angle)
# for i in range(f):
#     lily.color(random_color())
#     lily.circle(100)
#     lily.left(angle)


screen = t.Screen()
screen.exitonclick()