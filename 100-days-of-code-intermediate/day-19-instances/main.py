from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_off = 60
turtle_list = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-200, -150 + i * y_off)
    turtle_list.append(new_turtle)

is_race_on = True

while is_race_on:
    for i in range(0, 6):
        ran_dist = random.randint(0, 10)
        turtle_list[i].forward(ran_dist)
        if turtle_list[i].xcor() >= 230:
            winning_color = turtle_list[i].pencolor()
            is_race_on = False

if user_bet == winning_color:
    print(f"You've won! The {winning_color} turtle won the race!")
else:
    print(f"You've lost. The {winning_color} turtle won the race.")

# red_turtle = Turtle(shape="turtle")
# red_turtle.color(colors[0])
# red_turtle.penup()
# red_turtle.goto(-200, -150)
# orange_turtle = Turtle(shape="turtle")
# orange_turtle.color("orange")
# orange_turtle.penup()
# orange_turtle.goto(-200, -90)
# yellow_turtle = Turtle(shape="turtle")
# yellow_turtle.color("yellow")
# yellow_turtle.penup()
# yellow_turtle.goto(-200, -30)
# green_turtle = Turtle(shape="turtle")
# green_turtle.color("green")
# green_turtle.penup()
# green_turtle.goto(-200, 30)
# blue_turtle = Turtle(shape="turtle")
# blue_turtle.color("blue")
# blue_turtle.penup()
# blue_turtle.goto(-200, 90)
# purple_turtle = Turtle(shape="turtle")
# purple_turtle.color("purple")
# purple_turtle.penup()
# purple_turtle.goto(-200, 150)

screen.exitonclick()










# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def turn_ccw():
#     tim.left(10)
#
# def turn_cw():
#     tim.right(10)
#
# def clear_drawing():
#     tim.setpos(0, 0)
#     tim.clear()
#
# screen.listen()
#
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_ccw)
# screen.onkey(key="d", fun=turn_cw)
# screen.onkey(key="c", fun=clear_drawing)
