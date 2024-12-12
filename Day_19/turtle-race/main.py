import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race?: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []
y = -100



for color in colors:
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(color)
    tim.goto(x=-230, y=y)
    turtles.append(tim)
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f'You win! {turtle.pencolor()} is the winner!')
            else:
                print(f'You lost! {turtle.pencolor()} is the winner!')

        else:
            rand_distance = random.randint(0,20)
            turtle.forward(rand_distance)







screen.exitonclick()