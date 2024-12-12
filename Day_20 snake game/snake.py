from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
    
    def create_snake(self):
        for position in STARTING_POSITION:
            new_square = Turtle(shape='square')
            new_square.color('white')
            new_square.penup()
            new_square.goto(position)
            self.snake.append(new_square)
    
    def move(self):
        for seg_num in range(len(self.snake)-1,0,-1):
            new_x = self.snake[seg_num-1].xcor()
            new_y = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_x,new_y)

        self.snake[0].forward(MOVE_DISTANCE)    