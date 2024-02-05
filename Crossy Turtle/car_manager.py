import random
import turtle as t
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car():
    def __init__(self):
        self.all_cars = []
        self.car_speed = START_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1,6) #Reduce the rate cars are created
        if chance == 1:
            new_car = t.Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y_position = random.randint(-180, 180) # For the turtle to have some starting and ending position
            new_car.goto(300, rand_y_position)
            self.all_cars.append(new_car)
        
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT