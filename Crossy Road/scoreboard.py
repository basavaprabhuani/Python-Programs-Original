from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Coral")
        self.hideturtle()
        
    def game_over(self):
        
        self.write("GAME OVER", False, "center", FONT)


    
