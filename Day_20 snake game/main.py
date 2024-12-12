from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")


snake = []

for number in range(3):
    new_square = Turtle(shape='square')
    new_square.color('white')
    new_square.goto(x=-20*number,y=0)
    snake.append(new_square)




screen.exitonclick()