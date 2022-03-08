import turtle
from time import sleep
from random import randrange

wallsx = 300
wallsy = 200
delay = 0.1
paddleSpeed = 15
score = 0
highScore = 0
GameOver = False
playAgain = True


#functions

#Draw the border
def drawBorder():
  border.penup()
  border.goto(wallsx,wallsy)
  border.pendown()
  border.goto(wallsx,-wallsy)
  border.goto(-wallsx,-wallsy)
  border.goto(-wallsx,wallsy)
  border.goto(wallsx,wallsy)
  border.penup()

#Paddle up and Paddle Down
def paddleUp():
  paddle.sety(paddle.ycor() + paddleSpeed)
  if paddle.ycor() >= wallsy:
    paddle.sety(wallsy)

def paddleDown():
  paddle.sety(paddle.ycor() - paddleSpeed)
  if paddle.ycor() <= -wallsy:
    paddle.sety(-wallsy)

#set up turtles

#set up the Window
win = turtle.Screen()
win.setup(height=600,width=600)
win.title = ('Survival of the pongest')
win.bgcolor('black')
win.tracer(0)

#set up the border
border = turtle.Turtle()
border.speed(0)
border.color('white')
border.hideturtle()
drawBorder()

#create the paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.color('red')
paddle.penup()
paddle.goto(wallsx-40,0)
paddle.shapesize(4.0,0.5)

#Create the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('blue')
ball.penup()
ball.goto(paddle.xcor()-30,paddle.ycor())
ball.setheading(100)

#scores
pen = turtle.Turtle()
pen.speed(0)
pen.shape('circle')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: {} \n High Score:{}".format(score,highScore),align = 'center',font = ('center',24,'normal'))




 
while True:
  win.update()