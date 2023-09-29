import turtle
import pandas

# Create the screen
screen = turtle.Screen()
screen.title("Us States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create the turtle name of the state
pointer = turtle.Turtle()
pointer.hideturtle()
pointer.penup()

states = pandas.read_csv("50_states.csv")
states_list = states["state"].to_list()

correct_guesses = []

answer_state = screen.textinput(title="Guess the State", prompt="Qual o nome do próximo estado?").title()

while len(correct_guesses) < 50:
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in correct_guesses]
        data = pandas.DataFrame(missing_states)
        data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        correct_guesses.append(answer_state)

        state_singular = states[states.state == answer_state]

        state_xcor = int(state_singular.x)
        state_ycor = int(state_singular.y)

        pointer.goto(state_xcor, state_ycor)
        pointer.write(answer_state)

    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="Qual o nome do próximo estado?").title()











# pointer.reset()
# pointer.write("YOU WIN")
# screen.exitonclick()
