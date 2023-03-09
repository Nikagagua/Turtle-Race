from turtle import Turtle, Screen
from random import randint


is_race_on =False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color \n (Green/Red/Blue/Yellow/Purple): ").lower()
print(user_bet)
colors = ["green", "red", "blue", "yellow", "purple"]
y_pos = [100, 50, 0, -50, -100]
turtle_names = []




for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_pos[turtle_index])
    turtle_names.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_names:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The '{winning_color.capitalize()}'  turtle is the winner!")
            else:
                print(f"You've lost! The '{winning_color.capitalize()}' turtle is the winner!")

        turtle.forward(randint(0, 10))





screen.exitonclick()




