from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.color("white")
        self.width(20)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(position)
        self.showturtle()

    def go_up(self):
        new_y = self.ycor() + 20
        self.setpos(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.setpos(self.xcor(), new_y)