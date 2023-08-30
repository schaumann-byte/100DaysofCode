from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(0, 250)
        self.hideturtle()
        self.write(f"Score: {self.score}", align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 20, 'normal'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align='center', font=('Arial', 20, 'normal'))