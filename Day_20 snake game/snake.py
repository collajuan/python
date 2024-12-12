from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
    
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    
    def add_segment(self, position):
        new_square = Turtle(shape='square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(position)
        self.snake.append(new_square)

    def extend(self):
        self.add_segment(self.snake[-1].position())
    
    def move(self):
        for seg_num in range(len(self.snake)-1,0,-1):
            new_x = self.snake[seg_num-1].xcor()
            new_y = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_x,new_y)

        self.snake[0].forward(MOVE_DISTANCE)    
    
    def up(self):
        if self.snake[0].heading() != DOWN: 
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP: 
            self.snake[0].setheading(DOWN)

    def right(self):
        if self.snake[0].heading() != LEFT: 
            self.snake[0].setheading(RIGHT)
        

    def left(self):
        if self.snake[0].heading() != RIGHT: 
            self.snake[0].setheading(LEFT)
        