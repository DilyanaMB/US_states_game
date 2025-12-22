import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
guessed_states = []

data = pandas.read_csv('50_states.csv')
states = data.state.tolist()

# def get_mouse_click_coor(x, y):            # Getting coordinates when click upon screen, also keep screen open
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 Guess the State',
                                    prompt='What\'s another state\'s name?').title()

    if answer_state == 'Exit':
        missing_states=[state for state in states if state not in guessed_states]
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        raw = data[data.state == answer_state]
        t.goto(raw.x.item(), raw.y.item())
        t.write(answer_state)

not_guessed_states = list(set(states) - set(guessed_states))

not_guessed = pandas.DataFrame(not_guessed_states)
not_guessed.to_csv('states_to_learn.csv')
