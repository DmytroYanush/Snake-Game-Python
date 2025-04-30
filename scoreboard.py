from turtle import Turtle
X = 0
Y = 260
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(X, Y)
        self.show_score()

    def show_score(self):
        self.clear()
        express = f"Score: {self.score}"
        self.write(express, False, ALIGNMENT, FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", False, ALIGNMENT,FONT)

    def increase_score(self):
        self.score += 1
        self.show_score()