from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.position = position
        self.write_text()
        

    def write_text(self):
        self.clear()
        self.goto(self.position)
        self.write(f"Score: {self.score}", move=True, align="center")


    def increment_score(self):
        self.score +=1
        self.write_text()