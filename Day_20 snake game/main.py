import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)


new_snake = Snake()

game_si_on = True
while game_si_on:
    screen.update()
    time.sleep(0.1)

    new_snake.move()

screen.exitonclick()