# SESSDSA18课程上机作业
# 【H7】递归编程作业
# 本文件内编写编写递归算法，输出Pascal三角形（杨辉三角）
# pascalTriangle(numofrow)
# numofrow表示三角形有几行
# 每行的数字都是由上一行的对角线数字相加而得
# 可直接运行输出10阶三角形，阶数numofrow可以调整
#
# 在4月17日23：59前与其他文件打包提交到~新的作业提交系统~
#
# by TYY
# 2018/4/6


def pascalTriangle(numofrow,width=None):     #助教注意:我这里加了个参数控制输出宽度
    if width==None:
        width=numofrow*4
    if numofrow>0:
        lst=pascalTriangle(numofrow-1,width) #递归思路:先打印上面的小三角，再打印本行
        newlst=[1]
        for i in range(1,numofrow-1):
            newlst.append(lst[i]+lst[i-1])
        if numofrow>1:
            newlst.append(1)
        print('  '.join(map(str,newlst)).center(width))
        return newlst                        #把本行数据传给上一级函数(下一行)
    return None


# 测试
pascalTriangle(10)
