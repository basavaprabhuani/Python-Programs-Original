import random as r
from turtle import Turtle, Screen
import time
from player import Player
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


J = Player()
J.color("white")
screen = Screen()

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.STARTING = 14
        self.MOVE_INCREMENT = 10
        self.hideturtle()

    def create_car(self):
        screen.tracer(0)
        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.color(r.choice(COLORS))

        random_ycor = r.randint(-280, 280)
        random_xcor = r.randint(275, 350)
        new_car.goto(random_xcor, random_ycor)
        
        new_car.forward(15)
        time.sleep(0.2)
        if new_car.distance(J) < 50:
            new_car.clear()
        self.all_cars.append(new_car)
        screen.update()

    def move_car(self):
        for i in range(len(self.all_cars)):
    
            self.all_cars[i].backward(self.STARTING)

    def next_level(self):
        self.STARTING += self.MOVE_INCREMENT




    


    



