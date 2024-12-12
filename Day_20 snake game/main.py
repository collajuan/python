import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # next food
    if snake.snake[0].distance(food) < 15:
        score.incement_score()
        snake.extend()
        food.refresh()
    
    # detect wall
    if snake.snake[0].xcor() < -280 or snake.snake[0].xcor() > 280 or snake.snake[0].ycor() < -280 or snake.snake[0].ycor() > 280:
        game_is_on = False
        score.game_over()

    # Detect collision tail
    for segment in snake.snake[1:]:
        if snake.snake[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()