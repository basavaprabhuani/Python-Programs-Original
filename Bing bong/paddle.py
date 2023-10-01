from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 5)
        self.color("white")
        self.goto(x=350, y=0)
        self.left(90)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)


