from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)


paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score_board = Scoreboard()
screen.listen()

screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")


is_game_om = True
while is_game_om:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    elif ball.xcor() > 400:
        ball.reset_position()
        score_board.l_increase()

    if ball.xcor() < -400:
        ball.reset_position()
        score_board.r_increase()




















screen.exitonclick()