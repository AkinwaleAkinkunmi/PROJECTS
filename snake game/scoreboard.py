import turtle as t
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg = f"SCORE: {self.score}", align = ALIGNMENT, font = FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write(arg = f"GAME OVER", align = ALIGNMENT, font = FONT)

    def track_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
