from turtle import Turtle

class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(0, 260)
        self.current = 0

    def update(self):
        self.clear()
        self.current += 1
        self.write(f"Level: {self.current}", align="Left", font=("Arial", 24, "normal"))

    def game_over(self):
        self.setpos(0,0)
        self.write("Game Over", align="Center", font=("Arial", 48, "normal"))