import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name").title()
    print(answer_state)

missing_states = [state for state in all_states if state not in guessed_states]








    if answer_state == "Exit":
        missing_states = []
        for i in all_states:
            if i not in guessed_states:
                missing_states.append(i)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())



# input: state name
    #ignore: upper vs lowercase [DONE]

# process
    # num_correct
    # check if guess is in csv
    # if correct and new
        # num_correct +1
        # add state name using coordinates

    # if incorrect: no action

# display
    # initial: Guess a state
    # after initial: num_correct
