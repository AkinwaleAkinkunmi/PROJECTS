import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image) # Can be used to turn an image to a shape
turtle.shape(image)

# def get_mouse_click_coor(x, y): # Getting the coordinates of the mouse click on the turtle screen
#     print(x, y)


# t.onscreenclick(get_mouse_click_coor)
# t.mainloop()

playing = True

answer_states = screen.textinput(title=f"Guess a state", prompt= "What's another state name")
answer_states_title = answer_states.title()
states_data = pd.read_csv("50_states.csv")
states_list = states_data["state"].to_list()

if answer_states_title in states_list:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_row = states_data[states_data.state == answer_states]
    # t.goto(int(state_row.x), int(state_row.y))
    t.goto(int(state_row['x'].iloc[0]), int(state_row['y'].iloc[0])) # Gets the item in the x and y column    
    t.write(answer_states)

screen.exitonclick()
