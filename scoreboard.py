from lib2to3.fixes.fix_tuple_params import find_params
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-300,250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "left" , font= ("Courier", 24, "normal") )

    def increase_score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over", align="center", font =  ("Courier", 24, "normal"))

