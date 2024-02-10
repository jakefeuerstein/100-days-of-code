from turtle import Turtle

class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-260, 260)
        self.current = 0

    def update(self):
        self.clear()
        self.current += 1
        self.write(f"Level: {self.current}", align="left", font=("Arial", 24, "normal"))

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER")