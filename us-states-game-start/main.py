import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# # it is another way to keep the screen even our code finish running
# turtle.mainloop()



state_list = data["state"].to_list()
# data.state.to_list()
print(state_list)



guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states correct",
                                        prompt="What's another State's name?").title()



    if answer_state == "Exit":
        # missing_states =[]
        # for state in state_list:
        #     if state not in  guessed_state:
        #         missing_states.append(state)
        missing_states = [state for state in state_list if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_Learn.csv")
        print(missing_states)
        break
    if answer_state in state_list:
        guessed_state.append(answer_state)
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()

        n_state = data[data.state == answer_state]
        # x_arrey = int(n_state.x)
        # y_arrey = int(n_state.y)

        state_name.goto(int(n_state.x), int(n_state.y))

        state_name.write(answer_state, align='center', font=('Arial', 8, 'normal'))
        #  state_name.write(n_state.item())

States_to_Learn.csv


# screen.exitonclick()
