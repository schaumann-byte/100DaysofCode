from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Create the Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create the paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create the ball
ball = Ball()

# Create the scoreboard
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect Collision with Horizontal Walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle or left paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # Detect if R_Paddle misses
    if ball.xcor() > 380:
        ball.reset_round()
        scoreboard.l_point()

    # Detect if L_Paddle misses
    if ball.xcor() < -380:
        ball.reset_round()
        scoreboard.r_point()



screen.exitonclick()
