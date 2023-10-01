
import turtle
import pandas
import random

FONT = ("Gabriola", 15, "normal")

screen = turtle.Screen()
map = "India Map.gif"
screen.addshape(map)
mapp = turtle.Turtle()
mapp.shape(map)

states = pandas.read_csv("states_cor.csv")
state = states["state"].tolist()
x_cor = states["x"].tolist()
y_cor = states["y"].tolist()

trier = Turtle()
trier.hideturtle()
trier.penup()
guesses = []

answer = Turtle()
answer.hideturtle()
answer.penup()
answer.color(random.random(), random.random(), random.random())
game_is_on = True

while game_is_on:

    guess = screen.textinput(title="Guess the states", prompt="Guess a state:").title()

    if guess not in state:
        trier.goto(300, 0)
        trier.write("Try Again!", False, align="center", font=FONT)
    
    elif guess in state:
        index = state.index(guess)
        x = x_cor[index]
        y = y_cor[index]
        answer.goto(x, y)
        answer.write(guess, False, align="center", font=FONT)
        guesses.append(guess)

    if guess == "Give Up".title():
        for all in state:
            index = state.index(all)
            x = x_cor[index]
            y = y_cor[index]
            answer.goto(x, y)
            answer.write(all, False, align="center", font=FONT)

    if len(guesses) > 28:
        game_is_on = False

    




