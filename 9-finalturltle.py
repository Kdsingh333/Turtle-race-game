import turtle
import random
from typing import final


S = turtle.Screen()
S.setup(700, 500)
S.title("Turtle Race Game")
S.bgcolor("lightgreen")

# create pen
T = turtle.Turtle()
T.speed(0)

# start line
T.up()
T.setposition(-140, 50)
T.write("start line", align='center')
T.right(90)
T.forward(10)
T.down()
T.forward(155)

# finsih line
T.up()
T.setposition(140, 50)
T.write("finish line", align='center')
T.forward(10)
T.down()
T.forward(155)

# Track lines
T.up()
T.setposition(-170, 20)
T.color('white')
T.down()
T.left(90)
T.forward(340)

T.up()
T.setposition(-170, -10)
T.color('white')
T.down()
T.forward(340)

T.up()
T.setposition(-170, -40)
T.color('white')
T.down()
T.forward(340)

T.up()
T.setposition(-170, -70)
T.color('white')
T.down()
T.forward(340)

T.up()
T.setposition(-170, -100)
T.color('white')
T.down()
T.forward(340)

T.hideturtle()

# turtle.1

T1 = turtle.Turtle()
T1.up()
T1.setposition(-160, 10)
T1.shape("turtle")
T1.color("red")

# second turtle
T2 = turtle.Turtle()
T2.up()
T2.setposition(-160, -25)
T2.shape("turtle")
T2.color("blue")


# third turtle

T3 = turtle.Turtle()
T3.up()
T3.setposition(-160, -55)
T3.shape("turtle")
T3.color("green")

# fourth turtle

T4 = turtle.Turtle()
T4.up()
T4.setposition(-160, -85)
T4.shape("turtle")
T4.color("black")

line = 140

while T1.xcor() < line or T2.xcor() < line or T3.xcor() < line or T4.xcor() < line:
    T1.forward(random.randint(1, 5))
    T2.forward(random.randint(1, 5))
    T3.forward(random.randint(1, 5))
    T4.forward(random.randint(1, 5))

# decide ranking
finals_list = [T1.xcor(), T2.xcor(), T3.xcor(), T4.xcor()]
finals_dict = {T1.xcor(): 'red', T2.xcor(): 'blue', T3.xcor(): 'green', T4.xcor(): 'black'}

finals_list = sorted(finals_list, reverse=True)

# Ranking board

T.up()
T.color('black')
T.setposition(-60, 200)
T.write("Ranking Board", align="left", font=(None, 12))

# first place
T.setposition(-60, 180)
rank = finals_list[0]
T.write(f'1st place: {finals_dict[rank]} turtle', align='left')

# 2nd
T.setposition(-60, 160)
rank = finals_list[1]
T.write(f'2nd place: {finals_dict[rank]} turtle', align='left')

# 3rd
T.setposition(-60, 140)
rank = finals_list[2]
T.write(f'3rd place: {finals_dict[rank]} turtle', align='left')

# 4th
T.setposition(-60, 120)
rank = finals_list[3]
T.write(f'4th place: {finals_dict[rank]} turtle', align='left')


turtle.done()
