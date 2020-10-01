import turtle
from turtle import *

WIDTH = 1000
HEIGHT = 1000
setup(WIDTH,HEIGHT)
title("Recursive tree")


turtle_1 = turtle.Turtle() 

def setup_turtle(turtle):
    turtle.penup()
    turtle.left(90)
    turtle.sety(-HEIGHT/4)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pendown()

def set_position(turtle,position):
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()    
    
def draw_tree(turtle,depth,forward_step,angle):
    print(depth,forward_step,angle)
    
    
    if(depth == 0):
        return
    
    turtle.forward(forward_step)
    position = turtle.position()
    heading = turtle.heading()
    
    #left
    set_position(turtle,position)
    turtle.setheading(heading)
    
    turtle.left(angle)    
    draw_tree(turtle,depth-1,forward_step*0.80,angle)
    #right
    set_position(turtle,position)
    turtle.setheading(heading)
    
    turtle.right(angle)
    draw_tree(turtle,depth-1,forward_step*0.80,-angle)

setup_turtle(turtle_1)    
draw_tree(turtle_1,7,100,30)
