STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

import turtle as t

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        # Create a head attribute
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self,position):
        new_segment = t.Turtle(shape = "square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def grow_snake(self):
        self.add_segment(self.segments[-1].position()) #From the end of the list

    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):# To go backwards
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        # Don't allow the snake to go the opposite direction
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def move_down(self):
        if self.head.heading() != UP: 
            self.head.setheading(DOWN)
        
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    
         