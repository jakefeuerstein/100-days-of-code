#imports
from turtle import Screen, Turtle
import time
from player import Player
from level import Level
from random import randint
from car import Car

def check_car_collide(car_list):
    for car_i in car_list:
        for car_j in car_list:
            if car_list.index(car_i) != car_list.index(car_j) and car_i.distance(car_j) <= car_i.width() + 20:
                if car_i.xcor() > car_j.xcor():
                    car_i.move_speed = car_j.move_speed
                else:
                    car_j.move_speed = car_i.move_speed

#Create screen
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("white")

time_step = 0.1

player = Player()

level = Level()

cars = []

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
level.update()

while game_is_on:
    screen.update()
    time.sleep(time_step)
    for car_k in cars:
        car_k.move()
        check_car_collide(cars)
        if abs(player.xcor() - car_k.xcor()) <= 25 and abs(player.ycor() - car_k.ycor()) <= 15:
            level.game_over()
            game_is_on = False
            break
        if car_k.xcor() <= -320:
            cars.remove(car_k)
            del car_k
    ran_num = randint(1, 5)
    #Create car
    if ran_num == 1:
        car = Car(cars)
        cars.append(car)
    if player.ycor() >= 290:
        player.reset()
        level.update()
        time_step *= 0.01

    #     car.speedup()
    # if player.distance()


screen.exitonclick()