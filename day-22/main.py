from turtle import Screen, Turtle

# Create the Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create the paddle
paddle = Turtle()
paddle.color("white")
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def move_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def move_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()







screen.exitonclick()
