import time
import turtle as t
from player import Player
from car_manager import Car
from scoreboard import Scoreboard


screen = t.Screen()
screen.setup(width = 600, height = 500)
screen.tracer(0)

player = Player()
car_manager = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

playing = True 

while playing:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            playing = False
            scoreboard.game_over()

    # Detect when player has crossed the road
    if player.ycor() == 250:
        scoreboard.increase_level() 
        player.go_to_start()
        car_manager.increase_speed()  
        

screen.exitonclick( )