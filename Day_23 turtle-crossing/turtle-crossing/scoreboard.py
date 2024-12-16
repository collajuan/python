from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        # self.color("white")
        # self.write_text()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", move=True, align="left", font = FONT)
        

    def level_up(self):
        self.level += 1
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", move=True, align="left", font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=True, align="center", font = FONT)
