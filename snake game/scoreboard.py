import turtle as t
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0        
        with open("data.txt") as data:
            self.highscore = int(data.read()) # read returns as a string
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg = f"SCORE: {self.score} HIGH SCORE: {self.highscore}", align = ALIGNMENT, font = FONT)

    def reset_scoreboard(self):
        if self.score > self.highscore:  
            self.highscore = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg = f"GAME OVER", align = ALIGNMENT, font = FONT)

    def track_score(self):
        self.score += 1
        self.update_scoreboard()
    
