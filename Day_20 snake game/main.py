import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)


snake = []
for number in range(3):
    new_square = Turtle(shape='square')
    new_square.color('white')
    new_square.penup()
    new_square.goto(x=-20*number,y=0)
    snake.append(new_square)

game_si_on = True
while game_si_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(snake)-1,0,-1):
        new_x = snake[seg_num-1].xcor()
        new_y = snake[seg_num-1].ycor()
        snake[seg_num].goto(new_x,new_y)

    snake[0].forward(20)    

screen.exitonclick()