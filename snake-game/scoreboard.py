from turtle import Turtle
with open("data.txt") as file:
    h_score = file.read()


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(h_score)
        self.color("white")
        self.penup()
        self.setposition(0, 250)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write("GAME OVER", align='center', font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()