import turtle

wn = turtle.Screen()
wn.title("Pong by @azimsaidov")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

#score

score_a = 0
score_b = 0


#paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350, 0)



#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 1.5
ball.dy = 1.5


#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font=("Courier", 24, "normal"))


#FUNCTIONS


def paddle_a_up() :
  y = paddle_a.ycor()
  y += 25
  paddle_a.sety(y)


def paddle_a_down() :
  y = paddle_a.ycor()
  y -= 25
  paddle_a.sety(y)


def paddle_b_up() :
  y = paddle_b.ycor()
  y += 25
  paddle_b.sety(y)



def paddle_b_down() :
  y = paddle_b.ycor()
  y -= 25
  paddle_b.sety(y)

def end_game() :
  ball.dx = 0
  ball.dy = 0


#Keyboard Binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")

wn.listen()
wn.onkeypress(paddle_a_down, "s")

wn.listen()
wn.onkeypress(paddle_b_up, "Up")

wn.listen()
wn.onkeypress(paddle_b_down, "Down")



#main game loop
while True:
  wn.update()

  if score_a == 7 :
    end_game()
  
  if score_b == 7 :
    end_game()

  #Move Ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)
  
  #Border Check

  if ball.ycor() > 290 :
    ball.sety(290)
    ball.dy *= -1

  if ball.ycor() < -290 :
    ball.sety(-290)
    ball.dy *= -1

  if ball.xcor() > 390 :
    ball.goto(0,0)
    ball.dx *= -1
    pen.clear()
    score_a += 1
    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font=("Courier", 24, "normal"))


  if ball.xcor() < -390 :
    ball.goto(0,0)
    ball.dx *= -1
    pen.clear()
    score_b += 1
    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font=("Courier", 24, "normal"))


  #Paddle and Ball Collision Check

  if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40) :
    ball.setx(340)
    ball.dx *= -1

  if ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40) :
    ball.setx(-340)
    ball.dx *= -1


  

