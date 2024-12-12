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
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", move=True, align="center")

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=True, align="center", font=('Arial', 8, 'normal'))


    def incement_score(self):
        self.score +=1
        self.write_text()