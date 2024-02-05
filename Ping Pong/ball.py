import turtle as t

class Ball(t.Turtle):
    def __init__(self):
        super(). __init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_wall(self):
        # Reverses the direction of the ball(up to down and vice versa)
        self.y_move *= -1
    
    def bounce_paddle(self):
        # Reverses the direction of the ball from left to right and vice versa
        self.x_move *= -1
    
    def reset_position(self):
        self.goto(0,0)
        self.bounce_paddle() 

    def increase_speed(self):
        self.speed