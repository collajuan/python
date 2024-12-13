from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
ball = Ball()
score_player1 = Scoreboard((200, 280))
score_player2 = Scoreboard((-200, 280))

screen.listen()

screen.onkey(paddle1.move_up, 'Up')
screen.onkey(paddle1.move_down, 'Down')
screen.onkey(paddle2.move_up, 'w')
screen.onkey(paddle2.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.1)    
    screen.update()
    ball.move()
    
    # Collision up/down
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # collision player 1
    if ball.xcor() > 320 and paddle1.distance(ball) < 50 or ball.xcor() < -320 and paddle2.distance(ball) < 50:
        ball.bounce_x()
    
    
    #Punto para player 2
    if ball.xcor() > 360:
        ball.reset_position()
        score_player2.increment_score()

    #Punto para player 1
    if ball.xcor() < -360:
        ball.reset_position()
        score_player1.increment_score()
    


screen.exitonclick()