from turtle import Turtle, Screen

screen = Screen()
screen.listen()
while True:
    if screen.onkeypress(None, "Up"):
        print("yep")

screen.exitonclick()