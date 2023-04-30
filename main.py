from turtle import Turtle, Screen
import random as r

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you choose? Enter a color= ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles_colored = []
n = 0
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color)
    turtle.goto(x=-230, y=-110+n)
    n += 40
    turtles_colored.append(turtle)

is_race_on = True

while is_race_on:
    for n in range(6):
        if turtles_colored[n].xcor() > 230:
            is_race_on = False
            winner = turtles_colored[n].pencolor()
            if winner == user_bet:
                print(f"You've won!  The winner is {winner}.")
            else:
                print(f"You've lose!  The winner is {winner} one not {user_bet}.")
        turtles_colored[n].forward(r.randint(0,10))


screen.exitonclick()