import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):            # Getting coordinates when click upon screen, also keep screen open
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

answer_state = screen.textinput(title='Guess the State', prompt='What\'s another state\'s name?').title()
data =pandas.read_csv('50_states.csv')
states = data.state

for state in states:
    if state in answer_state:
        draw_state = turtle.Turtle()
        draw_state.hideturtle()
        draw_state.penup()
        raw =data[data.state == state]
        draw_state.goto(raw.x, raw.y)