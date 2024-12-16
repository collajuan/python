import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()

screen.listen()
screen.onkey(turtle.move, 'Up')

game_is_on = True
loop_number = 0
cars = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop_number += 1

    if loop_number == 6:
        loop_number = 0
        new_car = CarManager()
        cars.append(new_car)

    for car in cars:
        car.move()
