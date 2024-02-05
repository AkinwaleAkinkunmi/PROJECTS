import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard 
import time 

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)


left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard() 

screen.listen()
screen.onkey(fun= left_paddle.go_up, key="w")
screen.onkey(fun= left_paddle.go_down, key="s")
screen.onkey(fun= right_paddle.go_up, key="Up")
screen.onkey(fun= right_paddle.go_down, key="Down")

Playing = True
speed = 0.1

while Playing:
    time.sleep(speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect collision with right paddle
    if (
    ball.distance(right_paddle) < 50 and ball.xcor() > 320 or
    ball.distance(left_paddle) < 50 and ball.xcor() < -320
    ): 
        ball.bounce_paddle()
        speed /= 1.1

    # Detect when to score point
    
    if ball.xcor() > 380:# When right paddle misses
        ball.reset_position()
        scoreboard.l_point()
        speed = 0.1
        
    
    if ball.xcor() < -380: # When left paddle misses
        ball.reset_position()
        scoreboard.r_point()
        speed = 0.1

   # Detect a winner and game over 
    if scoreboard.r_score == 15 or scoreboard.l_score == 15:
        Playing = False
        scoreboard.game_over()
        
        


screen.exitonclick()