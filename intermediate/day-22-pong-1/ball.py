from turtle import Turtle
import random

SHAPE = "square"
WIDTH = 20
SPEED = 3
INIT_DIRECTION = (45, 135, 225, 315)
INIT_POS = (0, 0)
COLOR = "white"

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape(SHAPE)
        self.width(WIDTH)
        self.color(COLOR)
        self.setpos(INIT_POS)
        direction = random.choice(INIT_DIRECTION)
        self.seth(direction)
        self.tilt(-direction)
        self.speed(SPEED)
        self.showturtle()

    def move(self):
        self.forward(10)

    def collide(self):
        #Check if collide with upper and lower walls
        if self.ycor() >= (600/2 - WIDTH/2) or self.ycor() <= (-600/2 + WIDTH/2):
            self.seth(180 - self.heading())