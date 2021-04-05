from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


PADDLE = 360
BOUND = 10
WIDTH = 800
HEIGHT = 600
CORNER = 54 # 20の2乗と、50の2乗を足して、ルートしたもの（paddleの端に、ballが当たった時のballとpaddleの距離）

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # アニメーションをなくす

# ToDO: Paddle Classがあることにより、新しいPaddleを作成する時は1行追加すれば良いだけになる（クラスの大切さを感じて！）
r_paddle = Paddle((PADDLE, 0))
l_paddle = Paddle((PADDLE * -1, 0))

# ToDO: 真ん中のライン　dotにしたかったが、なんか変になった。
c_paddle = Paddle((0, 0))
c_paddle.turtlesize(stretch_wid=0.5, stretch_len=25)
c_paddle.shape("circle")
c_paddle.dot(0.5, "blue")


# ToDO: 押されているKeyを監視する
# a_key = WatchedKey('a')
# b_key = WatchedKey('b')

ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up) # functionの中には、変数を変えるmethodをかく　※雄一くんコメント
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1) # ゆっくりボールが進むようにする
    screen.update() # スクリーンをアップデートする。ゲームの世界
    ball.move()
    print("ball.x", ball.xcor(), "r_paddle", r_paddle.xcor())

    # 上下ボタンが押されていると、離されたというイベントを検知して、↑の状態を変更する
    # if upkey.key:
    #     r_paddle.move_up

    # ToDo: Detect collision with wall
    if ball.ycor() == -280 or ball.ycor() == 280:
        # print("壁に当たった")
        ball.bounce_y()

    # ToDo: Detect collision with r_paddle  ⭐️50を30にしたら、上の部分で当たっても、当たったと反応していない
    # 講師は、340（PADDLE - BOUND）を320にしている
    if (ball.xcor() == PADDLE - BOUND and r_paddle.distance(ball) < CORNER) or (ball.xcor() == PADDLE * -1 + BOUND and l_paddle.distance(ball) < CORNER) :
        print("paddleにぶつかった✌️")
        ball.bounce_x()

    # ToDo: If ball did not touch with the paddle, Update the scoreboard of the other side
    if ball.xcor() == PADDLE:
        print("r_paddleに当たらなかった😱")
        scoreboard.increase_l_score()
        ball.reset_position()

    if ball.xcor() == PADDLE * -1:
        print("l_paddleに当たらなかった😱")
        scoreboard.increase_r_score()
        ball.reset_position()

screen.exitonclick()