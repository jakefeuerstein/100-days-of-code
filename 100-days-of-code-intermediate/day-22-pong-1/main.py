from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

# Set screen constants
SCREEN_RATIO = 16 / 9
SCREEN_HEIGHT = 600
SCREEN_WIDTH = SCREEN_RATIO * SCREEN_HEIGHT
SCREEN_COLOR = "black"
SCREEN_TITLE = "Pong"

#Set net constants
NET_X = 0
NET_Y_START = 290
NET_WIDTH = 5
NET_DASH_LENGTH = 10
NET_DASH_SPACE = 10
NUM_DASHES = int((2 * NET_Y_START)/(NET_DASH_LENGTH + NET_DASH_SPACE))
NET_INIT_HEADING = 270
NET_COLOR = "white"
NET_SHAPE = "square"

#Time
TIME_STEP = 0.05

#Create screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)
screen.tracer(0)

#Create net
net = Turtle()
net.hideturtle()
net.penup()
net.shape(NET_SHAPE)
net.color(NET_COLOR)
net.width(NET_WIDTH)
net.setpos(NET_X, NET_Y_START)
net.seth(NET_INIT_HEADING)
# Draw net
for i in range(NUM_DASHES):
    net.pendown()
    net.forward(NET_DASH_LENGTH)
    net.penup()
    net.forward(NET_DASH_SPACE)

left_paddle = Paddle("left")
right_paddle = Paddle("right")

ball = Ball()

screen.listen()
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    #Detect and reflect horizontal wall collision
    if ball.ycor() >= (600 / 2 - ball.width() / 2) or ball.ycor() <= (-600 / 2 + ball.width() / 2):
        ball.seth(360 - ball.heading())
    # Detect and reflect paddle collision
    if ball.xcor() <= (left_paddle.xcor() - left_paddle.width() - ball.width()) and ball.ycor() <= \
            (left_paddle.ycor() - left_paddle.width() - ball.width()):
        ball.seth(180 - ball.heading())
    if abs(ball.xcor() - left_paddle.xcor()) <= (left_paddle.width()/2 + ball.width()/2) and abs(ball.ycor()\
            - left_paddle.ycor()) <= (left_paddle.width()/2 + ball.width()/2) or abs(ball.xcor() - right_paddle.xcor())\
            <= (right_paddle.width()/2 + ball.width()/2) and abs(ball.ycor()\
            - right_paddle.ycor()) <= (right_paddle.width()/2 + ball.width()/2):
    # if ball.distance(left_paddle) <= 10 or ball.distance(right_paddle) <= 10:
        ball.seth(180 - ball.heading())
    time.sleep(TIME_STEP)

screen.exitonclick()

