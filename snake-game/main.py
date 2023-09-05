from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# 1.Setup the Screen
screen = Screen()
screen.setup(width=585, height=585)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# 2. Create initial Snake and initial Food and initial Score
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# 3. Moving Snake
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detecting collision with wall
    if snake.head.xcor() > 280 or  snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
       scoreboard.reset()
       snake.reset_snake()
    # Detecting collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()


screen.exitonclick()

