from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.width(20)
        self.goto(0, 0)
        # self.seth(self.towards(400, 300))
        # self.tilt(-self.heading())
        self.showturtle()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddlebounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.hideturtle()
        self.goto(0, 0)
        self.move_speed = 0.1
        self.showturtle()