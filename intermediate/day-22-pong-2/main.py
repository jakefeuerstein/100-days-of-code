from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

l_score = 0
r_score = 0

scoreboard = Turtle()
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.color("white")
scoreboard.goto(0, 230)

time_sleep = 0.1
game_is_on = True
while game_is_on:
    time.sleep(time_sleep)
    scoreboard.clear()
    scoreboard.write(f"{l_score}  {r_score}", align="center", font=("Arial", 48, "normal"))
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddlebounce()
        time_sleep *= 0.5

    if ball.xcor() >= 380:
        l_score += 1
        ball.reset()

    if ball.xcor() <= -380:
        r_score += 1
        ball.reset()

screen.exitonclick()