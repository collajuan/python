from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write_text()

    def write_text(self):
        self.clear()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}  High score: {self.high_score}", move=True, align="center")

    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_text()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", move=True, align="center", font=('Arial', 8, 'normal'))


    def incement_score(self):
        self.score +=1
        self.write_text()