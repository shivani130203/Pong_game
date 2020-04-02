import turtle
import time
import winsound
wn=turtle.Screen()
wn.title("Pong by Shivani")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)



#score
score_a=0
score_b=0

#paddle a
paddle_a=turtle.Turtle() #Turle is class
paddle_a.speed(0);
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#paddle b
paddle_b=turtle.Turtle() #Turle is class
paddle_b.speed(0);
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=turtle.Turtle() #Turle is class
ball.speed(0);
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=1
ball.dy=1


#pen:for score
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0 Player B:0",align="center",font=("Courier",24,"normal"))
               
#endgame
end_game=turtle.Turtle()
end_game.speed(0)
end_game.color("red")
end_game.penup()
end_game.hideturtle()
end_game.goto(0,0)

#Functions

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)



def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)    

#keyboard
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#variable to decide that game is continuing or ending    
stop=0

#main game loop
while stop==0:
    wn.update()
    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    
    #border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy=ball.dy*-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)


    if ball.xcor()>380:
        ball.setx(380)
        ball.dx=ball.dx*-1
        score_b+=1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font=("Courier",24,"normal"));

    if ball.ycor()<-280:
        ball.sety(-280)
        ball.dy=ball.dy*-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.xcor()<-390:
        ball.setx(-390);
        ball.dx=ball.dx*-1
        score_a+=1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font=("Courier",24,"normal"));

    #bouncing off the paddles
    if ball.ycor()<paddle_b.ycor()+60 and ball.ycor()>paddle_b.ycor()-60 and ball.xcor()==330:
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.ycor()<paddle_a.ycor()+60 and ball.ycor()>paddle_a.ycor()-60 and ball.xcor()==-330:
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)


    #ending the game
    if score_a==5:
        end_game.write("Player B won",align="center",font=("Courier",24,"normal"))
        time.sleep(5)
        stop=1
        
    if score_b==5:
        end_game.write("Player A won",align="center",font=("Courier",24,"normal"))
        time.sleep(5)
        stop=1
        
        
        

