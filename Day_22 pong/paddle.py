from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.goto(position)
        

    def move_up(self):
        if self.ycor() < 240:
            new_y = int(self.ycor() + 20)
            self.goto(x=self.xcor(),y=new_y)
    
    def move_down(self):
        if self.ycor() > -240:
            new_y = int(self.ycor() - 20)
            self.goto(x=self.xcor(),y=new_y)

