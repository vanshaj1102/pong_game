from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score_1 = 0
        self.score_2 = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Player 1: {self.score_1}  Player 2: {self.score_2}", align="center", font=("Courier", 24, "normal"))

    def point_player_1(self):
        self.score_1 += 1
        self.update_score()

    def point_player_2(self):
        self.score_2 += 1
        self.update_score()

