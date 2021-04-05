from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, place):
        super().__init__()
        self.setheading(90)
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        # self.goto(350, 0)  # self.goto と self.placeの順序を逆にしたりすると、2つのpaddleが重なるように中央に配置されてしまう時の理由がわからない
        self.place = (self.xcor, self.ycor) # なんで、講師のは、この行がなくても、上手く動いている？
        self.color("white")
        self.penup()
        self.goto(place)

    def move_up(self):
        # paddle.setheading(0)
        self.forward(20)

    def move_down(self):
        # paddle.setheading(270)
        self.backward(20)

# https://stackoverflow.com/questions/58780485/python-turtle-check-if-a-key-is-down


# class WatchedKey(Screen):
#     def __init__(self, key):
#         super().__init__()
#         self.key = key
#         self.down = False
#         turtle.onkeypress(self.press, key)
#         self.onkeyrelease(self.release, key)
#
#     def press(self):
#         self.down = True
#
#     def release(self):
#         self.down = False



# 講師の方法
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)

