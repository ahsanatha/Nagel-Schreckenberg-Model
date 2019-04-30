import turtle  
import random as r
turtles = []
for i in range(2):
    turtles.append(turtle.Turtle())
x = 20
turtles[0].color('maroon')
turtles[1].color('pink')
turtles[0].penup()
for i in range(10):
    turtles[0].forward(x)
    turtles[0].left(30)
    turtles[1].forward(x)
      
turtle.done() 
