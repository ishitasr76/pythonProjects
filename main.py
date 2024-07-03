import turtle
import pandas
from turtle import Turtle, Screen
screen = Screen()
screen.title("US States Game")
# screen.setup(725,491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



num_correct_states = 0

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

# already_guessed = []
while num_correct_states<50:
    user_answer = screen.textinput(f"{num_correct_states}/50 States Correct", "What is another State")
    user_answer = user_answer.title()

    if user_answer in states:
        states.remove(user_answer)
        num_correct_states += 1
        state_name = Turtle()
        state_name.hideturtle()
        state_name.penup()
        row = data[data["state"] == user_answer]
        state_name. goto(int(row.x),int(row.y))
        state_name.write(user_answer, False, "center", ("Ariel", 8, "normal"))
    elif user_answer=="Exit":
        break

remaining_states_dict={}
remaining_states_dict["States you couldn't guess"] = states
learning = pandas.DataFrame(remaining_states_dict)
learning.to_csv("states_to_remember.csv")

