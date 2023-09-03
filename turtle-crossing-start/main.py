import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the turtle player
player = Player()

# Create the Car Manager
car_manager = CarManager()

# Create ScoreBoard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_player, "Up")

counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create Car
    if counter % 6 == 0:
        car_manager.create_car()
    car_manager.move_car()

    # Detect colision with cars
    for car in car_manager.garage:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.next_level()
        car_manager.increase_speed()
        scoreboard.next_level()

    counter += 1

screen.exitonclick()

#Final