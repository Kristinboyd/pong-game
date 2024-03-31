# Libraries
from turtle import *
import random
# constants
from constants import *


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLOR_LIST))
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", move=False, align=ALIGN_SCORE, font=FONT)
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", move=False, align=ALIGN_SCORE, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        self.color(random.choice(COLOR_LIST))

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        self.color(random.choice(COLOR_LIST))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align=ALIGN_SCORE, font=FONT)