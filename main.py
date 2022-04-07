from  turtle import Turtle, Screen
import random


screen=Screen()  # creating object for screen
game_on=True

screen.setup(width=700,height=600)  # setting up size of screen

colours=['red' , 'green','brown','yellow','blue','black']
y_cordinate=[220,120,0,-80,-180,-260]
turtles=[]

for x in range(0,6):
    new_turtle=Turtle(shape='turtle') #creating six turtle objects
    new_turtle.color(colours[x])
    new_turtle.penup()
    new_turtle.goto(x=-300, y=y_cordinate[x])  # setting up turtle coordinates
    turtles.append(new_turtle)  # appending the new turtle object
user_bet=screen.textinput(title='Make your bet',prompt='Which turtle will win')  #creating popup scree fornuser to make bet
while game_on:


    for x in turtles:
        rand_distance = random.randint(0, 10)
        x.forward(rand_distance)
        if x.xcor()> 320:     # checking the finishing line
            game_on=False
            winner=x.pencolor()  # pencolour() returns the colour of the instance
            if winner== user_bet:
                print(f"You have won the winner was {winner}")

            else:
                print(f"You have lost the winner was {winner}")

screen.exitonclick()

