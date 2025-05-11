from turtle import Turtle
X = 0
Y = 260
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(X, Y)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        express = f"Score: {self.score} High Score: {self.high_score}"
        self.write(express, False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.load_high_score))
        self.score = 0
        self.update_scoreboard()

    def load_high_score(self):
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()