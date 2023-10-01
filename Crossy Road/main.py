import time
from turtle import Screen
from player import Player
from car import CarManager
from scoreboard import Scoreboard

FONT = ("Courier", 24, "normal")
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    #DETECT COLLISION WITH CARS:    
    for car in car_manager.all_cars:
        if player.distance(car) < 17.5:
            game_is_on = False   
            scoreboard.penup()
            scoreboard.goto(0, 0)         
            scoreboard.game_over()

        


    else:
        pass
    
    
    #INCREASE LEVELS:
         
    if player.ycor() > 280:
        
        scoreboard.clear()
        a = 1
        a += 1
        player.orgplace()
        car_manager.next_level()
        

screen.exitonclick()
