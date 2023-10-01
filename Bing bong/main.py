from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Ping")
screen.tracer(0)

r_paddle = Paddle()
l_paddle = Paddle()
l_paddle.goto(-350, 0)
ball = Ball()


screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.listen()
game_on = True



boardr = Turtle()
boardr.penup()
boardr.color("coral")
boardr.hideturtle()
boardr.goto(x=360, y=240)

boardl = Turtle()
boardl.penup()
boardl.color("blue")
boardl.hideturtle()
boardl.goto(-360, -280)


l = 0
r = 0
while game_on:

    screen.update()
    ball.launch()

    #bounce when hit top or bottom:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        

    else:
        pass
    
    #detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    #detect out of bounds:
    #RIGHT SIDE
    if ball.xcor() > 390:
        r += 1
        boardr.clear()
        boardr.write(r, False, "left" , ("courier", 15, "normal"))
        ball.reset_position()
        
        
        

    #LEFT SIDE
    if ball.xcor() < -390:
        l += 1

        boardl.clear()
        boardl.write(l, False, "left" , ("courier", 15, "normal"))
        ball.reset_position()
        
        
        

screen.exitonclick()

