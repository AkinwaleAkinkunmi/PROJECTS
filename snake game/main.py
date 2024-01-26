import turtle as t
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Task 1 - Set the layout of the screen
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # Setting the screen background color
screen.title("Snake Game")  # Setting the title that is shown on the screen
screen.tracer(0)

# Task 2 - Create our snake body
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Task 4 - Controlling the snake with keyboard presses
screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right", )

# Task 3 - Moving the snake

screen.update()
time.sleep(0.1)
snake.move()

    # Create food and detect snake collision with food

if snake.head.distance(food) < 15:
    food.refresh()
    scoreboard.track_score()
    snake.grow_snake()



# Detect collision with wall
if (
    snake.head.xcor() > 280
    or snake.head.xcor() < -280
    or snake.head.ycor() > 280
    or snake.head.ycor() < -280
):
    scoreboard.reset_scoreboard()
    snake.reset_snake()
    

# Detect collision with body
for segment in snake.segments[1:]:  # List slicing
    if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()
        
screen.exitonclick()
