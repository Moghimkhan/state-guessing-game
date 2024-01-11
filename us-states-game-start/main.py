import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Set up the background image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load the data
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()

# Initialize guessed states list
guessed_states = []

# Game loop
while len(guessed_states) < 50:
    # Get user input for a state
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another state's name?").title()

    # Check if the user wants to exit
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states, columns=["state"])
        new_data.to_csv("States_to_Learn.csv", index=False)
        print(missing_states)
        break

    # Check if the guessed state is in the list
    if answer_state in state_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        # Get the coordinates for the guessed state
        state_data = data[data.state == answer_state]
        x_coordinate, y_coordinate = int(state_data.x), int(state_data.y)

        # Display the guessed state name on the map
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(x_coordinate, y_coordinate)
        state_name.write(answer_state, align='center', font=('Arial', 8, 'normal'))

# Close the turtle graphics window
turtle.mainloop()

