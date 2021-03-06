import turtle
import time
import random as r

wallsX = 300
wallsY = 200
delay = 0.025
direction = 0
paddleSpeed = 20
score = 0
highScore = 0
lengthMod = 4
widthMod = 0.5
ballXSpeed = 5
ballYSpeed = 5
speedBoostMod = 1.2
radius = 10
xv = -ballXSpeed
yv = -ballYSpeed

GameOver = False
playAgain = True

#functions


#Draw the border
def drawBorder():
    border.penup()
    border.goto(wallsX, wallsY)
    border.pendown()
    border.goto(wallsX, -wallsY)
    border.goto(-wallsX, -wallsY)
    border.goto(-wallsX, wallsY)
    border.goto(wallsX, wallsY)
    border.penup()


#Paddle up and Paddle Down
def paddleUp():
    paddle.sety(paddle.ycor() + paddleSpeed)
    if paddle.ycor() + (lengthMod * 10) >= wallsY:
        paddle.sety(wallsY - (lengthMod * 10)-1)


def paddleDown():
    paddle.sety(paddle.ycor() - paddleSpeed)
    if paddle.ycor() - (lengthMod * 10) <= -wallsY:
        paddle.sety(-wallsY + (lengthMod * 10)+1)


#Do movement stuff
def go_up():
    global direction
    direction = direction + 1


def go_down():
    global direction
    direction = direction - 1


#interpret direction
def interpretDirection():
    if direction == 1:
        paddleUp()
    elif direction == -1:
        paddleDown()


#Collisions
def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) <= (ball.radius + (
        (widthMod * 20) / 2)) and abs(a.ycor() - b.ycor()) < (ball.radius + (
            (lengthMod * 20) / 2))


#move ball
def moveBall():
    ball.setx(ball.xcor() + xv)

    ball.sety(ball.ycor() + yv)




def wallCollision():
  global xv, yv,GameOver,score
  if ball.xcor() <= -wallsX + ball.radius:
    ball.setx(-wallsX+ball.radius)
    xv = -xv
  if ball.ycor() <= -wallsY + ball.radius:
    ball.sety(-wallsY+ball.radius)
    yv = -yv
  if ball.ycor() >= wallsY - ball.radius:
    ball.sety(wallsY-ball.radius)
    yv = -yv
  if ball.xcor() >= wallsX - ball.radius:
    GameOver = True
    score = 0

#set up turtles

#set up the Window
win = turtle.Screen()
win.setup(height=600, width=600)
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
paddle.goto(wallsX - 40, 0)
paddle.shapesize(lengthMod, widthMod)

#Create the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('blue')
ball.penup()
ball.goto(paddle.xcor() - 70, paddle.ycor())
ball.radius = radius
ball.shapesize((ball.radius * 2) / 20)

#scores
pen = turtle.Turtle()
pen.speed(0)
pen.shape('circle')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {} \n High Score:{}".format(score, highScore),
          align='center',
          font=('center', 24, 'normal'))

# keyboard bindings
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeyrelease(go_down, "Up")
win.onkeyrelease(go_up, "Down")

while True:
    win.update()
    time.sleep(delay)
    interpretDirection()
    moveBall()
    if is_collided_with(paddle, ball):
        ball.setx(paddle.xcor()-ball.radius-(10*widthMod))
        xv = -xv
        score = score + 1
        xv = xv * r.uniform(1, speedBoostMod)
        yv = yv * r.uniform(1, speedBoostMod)
    wallCollision()
    if score > highScore:
        highScore = score
    pen.clear()
    pen.write("Score: {} \n High Score:{}".format(score, highScore),
              align='center',
              font=('center', 24, 'normal'))
    if GameOver == True:
        ball.goto(paddle.xcor() - 70, paddle.ycor())
        xv = -ballXSpeed
        yv = -ballYSpeed
        GameOver = False

      #written by Forcebender
