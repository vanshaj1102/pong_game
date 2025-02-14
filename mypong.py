import turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard

screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_1 = Paddle((-350, 0))
paddle_2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_1.move_up, "w")
screen.onkey(paddle_1.move_down, "s")
screen.onkey(paddle_2.move_up, "Up")
screen.onkey(paddle_2.move_down, "Down")

while True:
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if (ball.distance(paddle_1) < 50 and ball.xcor() < -330) or (ball.distance(paddle_2) < 50 and ball.xcor() > 330):
        ball.bounce_x()

    if ball.xcor() > 390:
        scoreboard.point_player_1()
        ball.reset_position()

    if ball.xcor() < -390:
        scoreboard.point_player_2()
        ball.reset_position()

screen.exitonclick()
