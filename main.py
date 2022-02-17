
import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(width=800, height=800)
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
tim = Turtle()
game_going = True
score = [0]

def game(score):
    answer_state = screen.textinput(title=f"{score[0]}/50 states correct", prompt="What is a states name?").title()

    states = pandas.read_csv("50_states.csv")

    if answer_state not in states.values:
        game(score)

    else:
        picked_state = states[states["state"] == answer_state]

        name = picked_state.iat[0, 0]
        x = picked_state.iat[0, 1]
        y = picked_state.iat[0, 2]
        score[0] = score[0] + 1
        tim.hideturtle()
        tim.penup()
        tim.goto(0, 300)

        tim.goto(x=x, y=y)
        tim.write(name, font=("Courier", 15, "normal"))
        screen.update()

while game_going:
    game(score)










