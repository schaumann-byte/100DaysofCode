FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-290, 250)
        self.color("black")
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def next_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.color("black")
        self.write(f"GAME OVER", align="center", font=FONT)

#Final