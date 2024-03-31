# Libraries
import time
import random
# Classes
from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Score
# Constants
from constants import *

# Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)


score = Score()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with roof or floor to re-bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        r_paddle.color(random.choice(COLOR_LIST))

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        l_paddle.color(random.choice(COLOR_LIST))

    # detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
