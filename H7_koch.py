# SESSDSA18课程上机作业
# 【H7】递归编程作业
# 本文件内编写Koch曲线代码
# 使用海龟制图，画出Koch曲线
# 可直接绘制5阶曲线，阶数n可以调整
#
# 在4月17日23：59前与其他文件打包提交到~新的作业提交系统~
#
# by TYY
# 2018/4/6

from turtle import Turtle,Screen

def KochCurve(tur,n,length):            #这里加了参数length，画横跨该长度的曲线
    if n>1:
        turn=(Turtle.left,Turtle.right) #转向函数集和转角参数
        argv=(60,120,60,0)
        for i in range(4):
            KochCurve(tur,n-1,length/3) #一条该曲线由四条低一阶曲线拼成
            turn[i%2](tur,argv[i])
    else:
        tur.forward(length)             #0阶曲线就是直线

# 测试
tur,scr=Turtle(),Screen()
scr.screensize(700,400)                 #初始化画布和乌龟
tur.pen(shown=False,pendown=False,speed=0)
tur.goto(-300,-100)
tur.down()
KochCurve(tur,5,600)
scr.exitonclick()