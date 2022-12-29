import turtle
from turtle import Turtle, Screen, colormode
import random

t = Turtle()
s = Screen()
s.setup(width=500, height=400)
t.penup()
colormode(255)
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
user_choice = s.textinput(title="Make your entry", prompt="Which turtle will win the race? Enter a color: ")
# print(user_choice)
# t.goto(-240, 0)
# no_of_turtles = int(s.textinput(title = "Number of turtles", prompt="How many turtles you want to see in the race? "))
# objects = []
# for each in range(no_of_turtles):
#     turtle_name = "t" + str(each)
#     objects.append(turtle_name)
#
# print(objects)
#
locY = [-70, -40, -10, 20, 50, 80]
not_at_wall = True
all_turtles = []
for index in range(6):
    # tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # print(tup)
    locX = -230
    turt = Turtle()
    turt.penup()
    turt.shape("turtle")
    turt.color(color_list[index])
    turt.goto(locX, locY[index])
    all_turtles.append(turt)

while not_at_wall:
    for tt in all_turtles:
        tt.forward(random.randint(0, 20))
        if tt.xcor()>220:
            print(tt.pencolor())
            not_at_wall = False
            if tt.pencolor() == user_choice :
                print("Your selected turtle won.")
            else:
                print(f"{tt.pencolor()} won, your selected turtle lost")



s.exitonclick()
