import random
import turtle as t
# import colorgram

lily = t.Turtle()
lily.pensize(3)
t.colormode(255)

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
print(color_list)
def random_color():
    ok = random.choice(rgb_colors)
    r = ok[0]
    g = ok[1]
    b = ok[2]
    colors = (r, g, b)
    # print(colors)
    return colors
# set_heading = lily.setheading(10)
# for i in range(12):
#     lily.color(random_color())
#
#     # lily.forward(20)
#     lily.dot(2)
#     current_heading = set_heading + 10


screen = t.Screen()
screen.exitonclick()