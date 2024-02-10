#Imports
from turtle import Screen, Turtle
from level import Level
from player import Player
from car import Car

#Create Screen
screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("white")

#Create Level Display
level = Level()

#Create Player
player = Player()

#Create Cars
car = Car()
cars = []

#Game Loop
game_is_on = True
time_step = 0.1
screen.listen()
screen.onkeypress(player.move(), "Up")

while game_is_on:
    screen.update()
    cars.move()
    if player.ycor() >= 300:
        player.reset()
        level.update()
        time_step *= 0.5
    for car_k in cars:
        if abs(player.xcor() - car_k.xcor()) <= 20 and abs(player.ycor() - car_k.ycor()) <= 20:
            level.gameover()
            game_is_on = False
            break

#Time step
#Get keyboard input
#Move player
#Move cars
#Update screen

#If player reaches end, increase level
#Incease car speed

#if player touches car, game over
