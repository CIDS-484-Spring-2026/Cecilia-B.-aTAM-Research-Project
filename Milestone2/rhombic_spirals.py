import sys
import math
import turtle
from turtle import *

#Draws a rhombus of a given major angle starting from the bottom left corner
def drawRhombus(theta):
    turtle.pd()
    turtle.forward(l)
    turtle.left(180-theta)
    turtle.forward(l)
    turtle.left(theta)
    turtle.forward(l)
    turtle.left(180-theta)
    turtle.forward(l)
    turtle.left(theta)
    turtle.pu()

#Set up variables
n = int(sys.argv[1]) if len(sys.argv) > 1 else 2 # number that determines theta and number of rotations
l = 100 # rhombus side length
theta = (180 * n) / (2*n -1) #major angle 
alpha = 180 - theta #minor angle
d = l * math.sin(math.radians(theta/2)) #distance from center to bottom left corner of rhombus

#Set up turtle
turtle.hideturtle()
turtle.degrees(360)
turtle.speed(0)
turtle.pu()

#Main Loop
i = 0
while (i < 2*n - 1): 
    #Moves us to bottom left corner relative to the center/0,0
    turtle.left(180 + (alpha/2))
    turtle.forward(d)

    #Resets the angle to the loop's staring angle
    turtle.right(180 + (alpha/2))

    drawRhombus(theta)

    #Reset to original position and rotate to draw next rhombus rotation
    turtle.teleport(0,0)
    turtle.left(alpha)
    i+=1

turtle.exitonclick()
