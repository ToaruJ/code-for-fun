# SESSDSA18课程上机作业
# 【H7】递归编程作业
# 本文件内编写分形树代码，可直接运行
# 修改分形树程序，增加如下功能：
# 树枝的粗细可以变化，随着树枝缩短，也相应变细
# 树枝的颜色可以变化，当树枝非常短的时候，使之看起来像树叶的颜色
# 让树枝倾斜角度在一定范围内随机变化，如15～45度之间，左右倾斜也可不一样，做成你认为最好看的样子
# 树枝的长短也可以在一定范围内随机变化，使得整棵树看起来更加逼真

# 在4月17日23：59前与其他文件打包提交到~新的作业提交系统~
#
# by TYY
# 2018/4/6


# 可自行添加函数，进行有创意的改造
from turtle import Turtle, Screen
from random import random, randrange
from time import sleep


def drawTree(tur, length, width):
    posi = tur.pos()
    tur.pen(pendown=True,pensize=int(width),
            pencolor=colorchange(length))                # 由树枝长度而变色，变宽度
    tur.forward(int(length))
    turnarg = ((15, 36), (-10, 10), (-35, -14))          # 随机转向的参数
    if length > 25:
        for i in range(3):
            if i != 1 or random() < 0.2:              # 树枝有0.2概率为三叉，一般是二叉
                rndangle = randrange(*turnarg[i])   # 随机数决定转向角和树枝长度变化
                rndlen = randrange(13, 25)
                tur.left(rndangle)
                drawTree(tur, length - rndlen,
                         width - rndlen * 2 / 15)
                tur.right(rndangle)
    else:
        if random() < 0.1:                          # 0.1概率生成红果子
            tur.dot(18, (224, 0, 0))
        else:                                     # 画出绿叶(随机长度)
            tur.pen(pencolor=(32, 192, 0), pensize=6)
            for i in range(3):
                rndangle = randrange(*turnarg[i])
                rndlen = randrange(10,20)
                tur.left(rndangle)
                tur.forward(rndlen)
                tur.backward(rndlen)
                tur.right(rndangle)
    tur.up()
    tur.goto(posi)


def colorchange(length):            # 返回颜色:树根(96,32,0)到小枝(64,128,0)变化
    return (int(64 + (96 - 64) * length / 150),
            int(128 + (32 - 128) * length / 150), 0)


# 测试
tur, scr = Turtle(), Screen()
tur.pen(shown=False, speed=1, pendown=False)          # 初始化画布和乌龟位置，朝向
scr.screensize(1280, 800)
scr.colormode(255)
scr.tracer(2)
tur.goto(0, -380)
tur.setheading(90)
sleep(2)
drawTree(tur, 150, 20)
scr.exitonclick()
