'''
SESSDSA18课程上机作业
【H3】Python类编程

说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
（1）直接在本文件中的函数体内编写代码，每个题目的函数后有调用语句用于检验，
上交作业时提交本文件，命名为h3_学号_姓名.py，如h3_1700000012_张三.py
（2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
（3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
（4）作业在3月19日 23：59之前提交到教学网


by TYY
2018.3.11
'''


'''
======= 1 People类 =======
创建一个People类，People 的属性有name 和age，两个参数在实例化的时候传给构造器，
People 类的方法有getName 和getAge，分别返回姓名和年龄。
'''
class People:
    def __init__(self, name, age):
        # 请在此编写你的代码(可删除pass语句)
        self.__name,self.__age=name,age
        # 代码结束
    def getName(self):
        # 请在此编写你的代码(可删除pass语句)
        return self.__name
        # 代码结束        
    def getAge(self):
        # 请在此编写你的代码(可删除pass语句)
        return self.__age
        # 代码结束  
# 调用检验
print("1-People")
p = People("Jack", 37)
print(p.getName(), p.getAge())


'''
======= 2 Student类 =======
创建一个Student 类，Student 类继承上一题中的People 类，
并且增加了属性id（表示学号），和方法getId。
'''
class Student(People):
    def __init__(self, name, age, id):
        # 请在此编写你的代码(可删除pass语句)
        People.__init__(self,name,age)
        self.__iden=id
        # 代码结束

    def getId(self):
        # 请在此编写你的代码(可删除pass语句)
        return self.__iden
        # 代码结束
# 调用检验
print("2-Student")
s = Student("Tess", 18, "1700000001")
print(s.getName(), s.getAge(), s.getId())


'''
======= 3 Xdict类 =======
创建一个Xdict类，继承自dict类(python中的字典类)，
使得Xdict类支持dict类的所有操作，并且增加一个方法getKeys，
用于返回给定值对应的键的列表。
例如：Xdict一个实例为xd = Xdict({2:"a", 3:"a", 4:(2,3)})，
则xd.getKeys("a")返回值为[2,3]
'''
class Xdict(dict):
    def getKeys(self, value):
        # 请在此编写你的代码(可删除pass语句)
        lst=[]
        for key in self.keys():
            if self[key]==value:
                lst.append(key)
        return lst
        # 代码结束

# 调用检验
print("3-Xdict")
xd = Xdict({2:"a", 3:"a", 4:(2,3)})
print(xd.getKeys("a"))


'''
======= 4 Vector类 ======
设计一个三维向量类，并实现向量的加法、减法以及向量与标量的乘法和除法运算
（要求三维向量转字符串方法str(向量对象)返回的结果为"(x,y,z)"的格式）。
提示：重写__init__,__add__,__sub__,__mul__,__truediv__,__str__方法
创建对象的方式为：v = Vector(x,y,z)
'''
class Vector:
    def __init__(self, x, y, z):
        # 请在此编写你的代码(可删除pass语句)
        self.__x=x
        self.__y=y
        self.__z=z
        # 代码结束
    def __add__(self, other):
        # 请在此编写你的代码(可删除pass语句)
        nx=self.__x+other.__x
        ny=self.__y+other.__y
        nz=self.__z+other.__z
        return Vector(nx,ny,nz)
        # 代码结束
    def __sub__(self, other):
        # 请在此编写你的代码(可删除pass语句)
        nx=self.__x-other.__x
        ny=self.__y-other.__y
        nz=self.__z-other.__z
        return Vector(nx,ny,nz)
        # 代码结束
    def __mul__(self, other):
        # 请在此编写你的代码(可删除pass语句)
        nx=self.__x*other
        ny=self.__y*other
        nz=self.__z*other
        return Vector(nx,ny,nz)
        # 代码结束
    def __truediv__(self, other):
        # 请在此编写你的代码(可删除pass语句)
        nx=self.__x/other
        ny=self.__y/other
        nz=self.__z/other
        return Vector(nx,ny,nz)
        # 代码结束
    def __str__(self):
        # 请在此编写你的代码(可删除pass语句)
        return "(%g,%g,%g)"%(self.__x,self.__y,self.__z)
        # 代码结束

# 调用检验
print("4-Vector")
v1 = Vector(1, 1, 2)
v2 = Vector(2, 4, 2)
print("v1 + v2：",v1+v2)
print("v1 - v2：",v1-v2)
print("v1 * 12：",v1*12)
print("v2 / 2：",v2/2)
