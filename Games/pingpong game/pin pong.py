# simple ping pong game using python3 for beginners
# By @SurajGavali

import turtle  #for graphical window

window = turtle.Screen()
window.title('Ping Pong by @SurajGavali') # for setting title of the window
window.bgcolor('black')
window.setup(width=1000,height=700)
window.tracer(0)  #stops updating window


score_A = 0
score_B = 0
#Left Pad

Left_pad = turtle.Turtle() # creating turtle object 
Left_pad.speed(0) #this is basically an animatio speed
Left_pad.shape('square')
Left_pad.color('white')
Left_pad.shapesize(stretch_wid=5,stretch_len=1)
Left_pad.penup() #turtle by default draw line while moving object we don't want that so we need to penup
Left_pad.goto(-450,0)

#Right Pad

Right_pad = turtle.Turtle() # creating turtle object 
Right_pad.speed(0) #this is basically an animatio speed
Right_pad.shape('square')
Right_pad.color('white')
Right_pad.shapesize(stretch_wid=5,stretch_len=1)
Right_pad.penup() #turtle by default draw line while moving object we don't want that so we need to penup
Right_pad.goto(440,0)


#Ball

Ball = turtle.Turtle() # creating turtle object 
Ball.speed(0) #this is basically an animatio speed
Ball.shape('circle')
Ball.color('white')
Ball.penup() #turtle by default draw line while moving object we don't want that so we need to penup
Ball.goto(0,0)
Ball.dx = 0.2
Ball.dy = 0.2

# Players information
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("Player A : {}  Player B : {}".format(score_A,score_B), align="center" , font=("Courier", 24, "normal"))

def Left_pad_up():
    current_y = Left_pad.ycor() #This returns current y co-ordinate
    current_y += 20
    Left_pad.sety(current_y)

def Left_pad_down():
    current_y = Left_pad.ycor() #This returns current y co-ordinate
    current_y -= 20
    Left_pad.sety(current_y)

def Right_pad_up():
    current_y = Right_pad.ycor() #This returns current y co-ordinate
    current_y += 20
    Right_pad.sety(current_y)

def Right_pad_down():
    current_y = Right_pad.ycor() #This returns current y co-ordinate
    current_y -= 20
    Right_pad.sety(current_y)


#keyboard  binding

window.listen() #listens for keyboard input
window.onkeypress(Left_pad_up,'w') #on pressing w pad moves up
window.onkeypress(Left_pad_down,'s') #on pressing s pad moves down
window.onkeypress(Right_pad_up,'Up') #on pressing w pad moves up
window.onkeypress(Right_pad_down,'Down') #on pressing s pad moves down

# main game loop

while True:
    window.update()

    #For moving ball

    Ball.setx(Ball.xcor() + Ball.dx) # moves ball in x direction
    Ball.sety(Ball.ycor() + Ball.dy) # moves ball in y direction

    #Border checking

    if Ball.ycor() > 340:
        Ball.sety(340)
        Ball.dy *= -1

    if Ball.ycor() < -330:
        Ball.sety(-330)
        Ball.dy *= -1

    if Ball.xcor() > 485:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_A,score_B), align="center" , font=("Courier", 24, "normal"))

    if Ball.xcor() < -485:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_A,score_B), align="center" , font=("Courier", 24, "normal"))



    #paddle and ball collision

    if(Ball.xcor() > 420 and Ball.xcor() < 440) and (Ball.ycor() < Right_pad.ycor() + 40 and Ball.ycor() > Right_pad.ycor() - 40):
        Ball.setx(420)
        Ball.dx *= -1

    if(Ball.xcor() < -430 and Ball.xcor() > -450) and (Ball.ycor() < Left_pad.ycor() + 40 and Ball.ycor() > Left_pad.ycor() - 40):
        Ball.setx(-430)
        Ball.dx *= -1
