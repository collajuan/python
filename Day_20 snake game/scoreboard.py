from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write_text()

    def write_text(self):
        self.clear()
        self.goto(x=0,y=270)
        self.write(f"Score: {self.score}", move=True, align="center")


    def incement_score(self):
        self.score +=1
        self.write_text()