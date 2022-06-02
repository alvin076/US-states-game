import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()

df = pd.read_csv('50_states.csv')
correct_guess = 0
guessed_state = []

while True:

    answer_state = screen.textinput(title=f'{correct_guess}/50 States Correct', prompt='What\'s another state\'s name?').title()

    if answer_state in df.state.to_list():
        guessed_state.append(answer_state)
        x, y = int(df[df['state'] == answer_state].x), int(df[df['state'] == answer_state].y)
        turtle.goto(x, y)
        turtle.write(answer_state)
        correct_guess += 1

    if answer_state == 'Exit':
        break

all_states = df.state.to_list()
for state in guessed_state:
    if state in all_states:
        all_states.remove(state)

state_left = {'state': all_states}
new_df = pd.DataFrame(state_left)
new_df.to_csv('states_to_learn.csv')