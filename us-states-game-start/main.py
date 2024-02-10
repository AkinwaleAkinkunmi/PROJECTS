import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image) # Can be used to turn an image to a shape
t.shape(image)

# def get_mouse_click_coor(x, y): # Getting the coordinates of the mouse click on the turtle screen
#     print(x, y)


# t.onscreenclick(get_mouse_click_coor)
# t.mainloop()

playing = True

while playing:
    answer_states = screen.textinput(title=f"Guess a state", prompt= "What's another state name")
    answer_states_title = answer_states.title()
    states_data = pd.read_csv("50_states.csv")
    states_list = states_data["state"].to_list()
    
    for state in states_list:
        if answer_states_title == state:
            

