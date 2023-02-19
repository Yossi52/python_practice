import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.setup(750,550)
screen.addshape(image)
turtle.shape(image)

state_name_writer = turtle.Turtle()
state_name_writer.penup()
state_name_writer.hideturtle()

# # 마우스 클릭하는 위치의 x, y 좌표를 출력해 줌
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
correct_guess = []


while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 State Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in states:
            if state not in correct_guess:
                missing_state.append(state)
        df_missing = pandas.DataFrame(missing_state)
        df_missing.to_csv("state_to_learn.csv")
        break

    if answer_state in states and answer_state not in correct_guess:
        correct_guess.append(answer_state)
        state_data = data[data.state == answer_state]
        state_name_writer.goto(int(state_data.x), int(state_data.y))
        state_name_writer.write(answer_state, align='center', font=('Corbel', 9, 'bold'))

