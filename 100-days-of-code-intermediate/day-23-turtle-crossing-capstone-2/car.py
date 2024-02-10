from turtle import Turtle
from random import randint, choice

colors = ["red", "blue", "green", "yellow"]

class Car(Turtle):

    def __init__(self, car_list, time_step):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.lane = randint(-6, 6)
        self.move_speed = randint(5, 10)
        self.check_car_collide_initial(car_list, time_step)
        self.shape("square")
        self.seth(0)
        self.width(40)
        self.setpos(320, self.lane*self.width())
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(colors))
        self.showturtle()

    def move(self):
        self.setx(self.xcor() - self.move_speed)

    def check_car_collide_initial(self, car_list, time_step):
        for car_k in car_list:
            if self.lane == car_k.lane:
                if self.distance(car_k.pos()) <= self.width()*2:
                    self.lane += 1
                    self.check_car_collide_initial(car_list, time_step)
                    # or self.distance(car_k.pos()) - 80 <= 600 and self.move_speed >= car_k.move_speed + \
                    #     (self.distance(car_k.pos()) - 80) * time_step:
                    # self.lane += 1
                    # self.check_car_collide_initial(car_list, time_step)