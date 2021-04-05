from turtle import Turtle
import random
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        # ToDO: ランダムに場所を動かそうとしたが、その方法では少しずつ動くということができないのか確かめる⭐️
        # self.pendown()
        # random_x = random.randint(-15, 15) * 20
        # random_y = random.randint(-25, 25) * 20
        # self.goto(random_x, random_y)

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # ToDO: Detect Collision with wall and bounc　（バウンドした時の表現の仕方がわからなかった）
    def bounce_y(self):
        # ToDO: 角度で書き表す方法がわからなかった
        # current_angle = self.heading()
        # self.right(360 - current_angle) # これで角度が変わっているように見えるが、forwardで進んだ後、また下の角度に戻ってしまっている。
        # self.forward(200)

        self.y_move *= -1

    def bounce_x(self):
        # ToDO: 角度で書き表す方法がわからなかった
        # current_angle = self.heading()
        # self.right(360 - current_angle) # これで角度が変わっているように見えるが、forwardで進んだ後、また下の角度に戻ってしまっている。
        # self.forward(200)

        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()