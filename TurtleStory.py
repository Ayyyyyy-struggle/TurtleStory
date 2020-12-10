## import turtle and time library
import turtle
import time

## declare global Variable
color = ['']*7
color = ['red','green','brown','lime','white','black','mistyrose']

## define a mountain climbing function with 2 parameters
def Climbing(mountain_color,line_depth):
    ## call out resetting function to start
    Resetting()
    turtle.shape('turtle')
    i = 0
    ## use loop to draw steps
    while i < 4:
        turtle.pencolor(mountain_color)
        turtle.pensize(line_depth)
        turtle.pendown()
        for i in range (0, 4):
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            turtle.right(90)
        turtle.forward(50)
        i = i + 1
    ## call out Writing function to write message
    Writing('Hurray! Made it to the top!')

## define a swimming function with 2 parameters    
def Swimming(path_color, thickness):
    ## call out resetting function
    Resetting()
    turtle.goto(-150,100)
    turtle.pendown()
    ## draw a circle and fill it with blue color
    turtle.color('blue')
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()

    ## draw another circle as turtle path with no filling
    turtle.penup()
    turtle.goto(-150,80)
    turtle.pendown()
    turtle.color(path_color,'green')
    turtle.shape('turtle')
    turtle.pensize(thickness)
    turtle.circle(100)
    ## turn turtle head to pool direction
    turtle.left(90)

    turtle.pencolor('blue')
    turtle.goto(-150,150)
    ## call writing function to write message
    Writing('Yeah! I\'m swimming!')

## define eating function without any parameter    
def Eating():
    ## call out resetting and declare local variables
    Resetting()
    location = [0]*2
    location = [-150,-150]
    i = 0
    ## use loop to draw 4 circles with different color
    while i < 4:
        for i in range(0,4):
            turtle.goto(location)
            turtle.pendown()
            turtle.color(color[i])
            turtle.begin_fill()
            turtle.circle(10)
            turtle.end_fill()
            location[0]=location[0] + 8
            location[1]=location[1] + 8
        i = i + 1
        location = [-150,-150]

    ## another loop to draw 4 same circles with white color
    for i in range(0,4):
        turtle.color(color[4])
        turtle.shape('turtle')
        turtle.penup()
        turtle.goto(location)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(11)
        turtle.end_fill()
        turtle.color(color[1])
        ## use time to have turtle stay for a second
        time.sleep(1)
        location[0] = location[0] + 8
        location[1] = location[1] + 8
    ## call out Writing function
    Writing('Wow! What a great meal!')

## define Sleeping function    
def Sleeping():
    ## call out restting and declare local varibales
    Resetting()
    location = [0]*2
    location = [150,-150]
    color2 = ['']*2
    color2 = [color[2],color[6]]
    square_side = 80
    ## use outter loop to draw 2 different squares
    ## inner loop to draw a square
    for i in range(0,2):
        turtle.penup()
        turtle.goto(location)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color2[i])
        for square in range(0,4):
            turtle.forward(square_side)
            turtle.left(90)
        turtle.end_fill()
        location[0]=location[0]+30
        location[1]=location[1]+40
        square_side = square_side - 60
    ## turtle go to center spot 
    turtle.goto(190,-110)
    turtle.left(90)
    turtle.shape('turtle')
    turtle.color(color[5],color[1])
    ## call out writing function
    Writing('Good Night!')

## define function to reset screen     
def Resetting():
    turtle.reset()
    turtle.penup()
    turtle.shape('classic')

## define writing function to write messages and let it stay for 3 seconds
def Writing(message):
    turtle.pencolor(color[5])
    turtle.write(message,False,align='right',font=('Arial',16,'bold'))
    time.sleep(3)

## main function to call out all 4 functions    
def main():
    turtle.setup(800,600)
    Climbing(color[2],5)
    Swimming(color[2],1)
    Eating()
    Sleeping()

main()
