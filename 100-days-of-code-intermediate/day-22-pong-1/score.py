from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 48, "normal")
SCORE_X = 50
SCORE_Y = 250
INIT_SCORE = 0

class Score(Turtle):

    def __init__(self, side):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.score = INIT_SCORE
        self.sety(SCORE_Y)
        if side == "left":
            self.setx(-SCORE_X)
        else:
            self.setx(SCORE_X)
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)