
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


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_date = data[data.state == answer_state]
        t.goto(int(state_date.x), int(state_date.y))
        t.write(answer_state)


states_to_learn = []

for state in all_states:
    if state not in guessed_states:
        states_to_learn.append(state)

states_df = pandas.DataFrame(states_to_learn)
states_df.to_csv("states.to.learn.csv")















