# SESSDSA18课程上机作业
# 【H7】递归编程作业
# （兴趣题，非必须）
# 本文件内编写汉诺塔动画代码，
# 用海龟制图，将河内塔解决过程做成动画
# 可以将海龟shape改为方块的盘子
# 将每个盘子都生成一个海龟
# penup方式移动海龟即可
# 可直接运行进行5盘片动画，盘片数量可以调整
#
# 在4月17日23：59前与其他文件打包提交到~新的作业提交系统~
#
# by TYY
# 2018/4/6

from turtle import Turtle, Screen
from time import sleep


class Pole:                                # 定义"柱子"类，属性为存盘片的列表
    def __init__(self, posx):               # 和柱子横坐标
        self.lst = []
        self.x = posx

    def add(self, tur):                     # 向柱子中加盘片，开始时用
        tur.hideturtle()
        tur.goto(self.x, 20 * len(self.lst) - 75)
        tur.showturtle()
        self.lst.append(tur)

    def move(self, topole):                 # 把self柱的最上面盘片移到topole柱
        tur = self.lst.pop()
        tur.goto(self.x, 90)
        tur.goto(topole.x, 90)
        tur.goto(topole.x, 20 * len(topole.lst) - 75)
        topole.lst.append(tur)
        sleep(1)


def drawHanoi(n):                          # 移动盘片主函数，可支持7个盘片
    A, B, C = Pole(-300), Pole(0), Pole(300)
    collst = ('red', 'orange', 'yellow',
              'green', 'cyan', 'blue', 'violet')
    for i in range(n):                     # 到line47:向A柱子加入盘片(先设置乌龟)
        newtur = Turtle()
        newtur.shape('square')
        newtur.shapesize(1, 2 * (n - i))
        newtur.pen(speed=4, pendown=False, fillcolor=collst[i])
        A.add(newtur)
    sleep(2)
    hanoi(n, A, B, C)


def hanoi(n, frompole, topole, withpole):     # 计算如何移动的递归函数
    if n > 0:
        hanoi(n - 1, frompole, withpole, topole)
        frompole.move(topole)
        hanoi(n - 1, withpole, topole, frompole)


# 测试
canv, scr = Turtle(), Screen()                 # 到line71:设置背景参数，在背景画好三根柱子
scr.screensize(900, 300)
canv.pen(shown=False, pensize=8, pendown=False, speed=0)
canv.goto(-450, -90)
canv.down()
canv.forward(900)
canv.left(90)
xpole = (-300, 0, 300)
for i in range(3):
    canv.up()
    canv.goto(xpole[i], -90)
    canv.down()
    canv.forward(160)
drawHanoi(5)
scr.exitonclick()
