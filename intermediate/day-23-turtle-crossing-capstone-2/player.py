from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.seth = 90
        self.setpos(0,-290)

    def move(self):
        self.sety(self.ycor() + 10)

    def reset(self):
        self.hideturtle()
        self.sety(-290)
        self.showturtle()

