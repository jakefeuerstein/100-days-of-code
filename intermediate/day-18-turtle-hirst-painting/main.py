from turtle import Turtle, Screen
from random import choice

# import colorgram
#
# colors = colorgram.extract('image.jpg', 10)
# rgb_list = []
# for color in colors:
#     rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_list.append(rgb)
# print(rgb_list)

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157)]

l_side = 250
num_cols = 10
num_rows = num_cols
dot_dist = 50

tim = Turtle()
tim.speed(0)
tim.hideturtle()
tim.penup()
tim.setpos(-l_side, l_side)

def make_dot_row():
    for i in range(num_cols):
        tim.pencolor(choice(color_list))
        tim.dot(20)
        tim.forward(50)

def next_row():
    tim.setpos(-250, tim.ycor() - dot_dist)

screen = Screen()
screen.colormode(255)

for i in range(num_rows):
    make_dot_row()
    next_row()

# print(tim.color())
# print(choice(color_list))

screen.exitonclick()
