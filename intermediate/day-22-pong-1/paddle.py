from turtle import Turtle, Screen

PADDLE_X = 400
PADDLE_WIDTH = 20
PADDLE_ASPECT_RATIO = 3
SEG_SHAPE = "square"
SEG_COLOR = "white"
UP = 90
DOWN = 270
DISTANCE = 20
SPEED = 10

screen = Screen()

class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape(SEG_SHAPE)
        self.width(PADDLE_WIDTH)
        self.shapesize(1, PADDLE_ASPECT_RATIO)
        self.color(SEG_COLOR)
        self.seth(UP)
        if side == "left":
            self.setpos(-PADDLE_X, 0)
        else:
            self.setpos(PADDLE_X, 0)
        self.speed(SPEED)
        self.showturtle()

    def up(self):
        self.seth(UP)
        self.forward(DISTANCE)

    def down(self):
        self.seth(DOWN)
        self.forward(DISTANCE)
