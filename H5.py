# SESSDSA18课程上机作业
# 【H5】栈与队列编程作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中的函数体内编写代码，每个题目的函数后有调用语句用于检验，
# 上交作业时提交本文件，命名为h5_学号_姓名.py，如h5_1700000012_张三.py
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业在4月3日23：59之前提交到教学网
#
#
# by TYY
# 2018.3.21


# ======= 1 中缀表达式求值 =======
# 通过把“中缀转后缀”和“后缀求值”两个算法功能集成在一起（非简单的顺序调用），
# 实现对中缀表达式直接求值，新算法还是从左到右扫描中缀表达式，
# 但同时使用两个栈，一个暂存操作符，一个暂存操作数，来进行求值。
#
# 创建一个函数，接受参数为一个字符串，即一个中缀表达式，
# 其中每个数字或符号间由一个空格隔开；
# 返回一个整数，即求值的结果。（支持 + - * / ^ 五种运算）
# 输入样例1：
# ( 2 + 3 ) * 6 + 4 / 2
# 输出样例1：
# 32
# 输入样例2：
# 2 ^ 3 + 4 * 5 - 16 / 2
# 输出样例2：
# 20
# 输入样例3：
# ( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6
# 输出样例3：
# 1


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def calculate(s):
    # 请在此编写你的代码（可删除pass语句）
    def opr(b,op,a):
        if op=='+': return a+b
        elif op=='-': return a-b
        elif op=='*': return a*b
        elif op=='/': return a/b
        else: return a**b
    prec={'(':1,'+':2,'-':2,'*':3,'/':3,'^':4}    #运算符优先级列表
    op,num=Stack(),Stack()      #生成两个栈，储存运算符和数字
    tokenlst=s.split(' ')
    for token in tokenlst:      #对元素分类操作
        if token=='(':
            op.push(token)
        elif token==')':
            while op.peek()!='(':
                num.push(opr(num.pop(),op.pop(),num.pop()))
            op.pop()
        elif token in '+-*/^':
            while (not op.isEmpty()) and \
            prec[op.peek()]>=prec[token]:
                num.push(opr(num.pop(),op.pop(),num.pop()))
            op.push(token)
        else:
            num.push(int(token))
    while not op.isEmpty():     #把未使用的运算符使用
        num.push(opr(num.pop(),op.pop(),num.pop()))
    return int(num.pop())
    # 代码结束

# 调用检验
print("1-calculate")
print(calculate("( 2 + 3 ) * 6 + 4 / 2"))
print(calculate("2 ^ 3 + 4 * 5 - 16 / 2"))
print(calculate("( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6"))


# ======= 2 基数排序 =======
# 实现一个基数排序算法，用于10进制的正整数从小到大的排序。
#
# 思路是保持10个队列(队列0、队列1......队列9、队列main)，开始，所有的数都在main队列，没有排序。
# 第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第三趟放百位，再合并；第四趟放千位，再合并。
# 直到最多的位数放完，合并完，这样main队列里就是排好序的数列了。
#
# 创建一个函数，接受参数为一个列表，为需要排序的一系列正整数，
# 返回排序后的数字列表。
# 输入样例1：
# [1, 2, 4, 3, 5]
# 输出样例1：
# [1, 2, 3, 4, 5]
# 输入样例2：
# [8, 91, 34, 22, 65, 30, 4, 55, 18]
# 输出样例2：
# [4, 8, 18, 22, 30, 34, 55, 65, 91]

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def radix_sort(s):
    # 请在此编写你的代码（可删除pass语句）
    main=Queue()
    for item in s:
        main.enqueue(item)
    lst=[Queue() for i in range(10)]
    flag,exp=True,0    #判断循环和记录比较的位数
    while flag:
        flag=False
        while not main.isEmpty():
            num=main.dequeue()
            lst[(num//10**exp)%10].enqueue(num)
            if (num//10**(exp+1))%10!=0:
                flag=True            #若该数下一位不是0，则需再循环
        for que in lst:
            while not que.isEmpty():
                main.enqueue(que.dequeue())
        exp+=1
    return [main.dequeue() for i in range(main.size())]
    # 代码结束

# 调用检验
print("2-sort")
print(radix_sort([1, 2, 4, 3, 5]))
print(radix_sort([8, 91, 34, 22, 65, 30, 4, 55, 18]))


# ======= 3 HTML =======
# 实现扩展括号匹配算法，用来检查HTML文档的标记是否匹配。
# HTML标记应该成对、嵌套出现，
# 开标记是<tag>这种形式，闭标记是</tag>这种形式。
#
# 创建一个函数，接受参数为一个字符串，为一个HTML文档中的内容，
# 返回True或False，表示该字符串中的标记是否匹配。
# 输入样例1：
# <html> <head> <title> Example </title> </head> <body> <h1>Hello, world</h1> </body> </html>
# 输出样例1：
# True
# 输入样例2：
# <html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>
# 输出样例2：
# False

def HTMLMatch(s):
    # 请在此编写你的代码（可删除pass语句）
    tag=Stack()
    for index in range(len(s)):
        if s[index]=='<':
            start=index       #记录标签起点位置
        elif s[index]=='>':
            if s[start+1]=='/':
                if tag.isEmpty() or tag.pop()!=s[start+2:index]:
                    return False    #标签不匹配，错误
            else:
                tag.push(s[start+1:index])    #标签入栈
    return tag.isEmpty()
    # 代码结束

# 调用检验
print("3-HTMLMatch")
print(HTMLMatch("<html> <head> <title>Example</title> </head> <body> <h1>Hello, world</h1> </body> </html>"))
print(HTMLMatch("<html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>"))

# ======= 4 击鼓传花 =======
# 将热土豆问题的模拟程序，修改为模拟"击鼓传花"，
# 即每次传递数不是常量值，而是一个随机数。
#
# 创建一个函数，接受一个参数，为一个人名列表，
# 返回经过击鼓传花后最后一个人的的人名。

def Game(namelist):
    # 请在此编写你的代码（可删除pass语句）
    from random import randrange
    nameque=Queue()
    for item in namelist:
        nameque.enqueue(item)
    while nameque.size()>1:
        pas=randrange(nameque.size())      #随机生成数，表示通过pas个人后传到
        for i in range(pas):
            nameque.enqueue(nameque.dequeue())
        nameque.dequeue()
    return nameque.dequeue()
    # 代码结束

# 调用检验
print("4-Game")
print(Game(['Lily', 'Monica', 'Alex', 'Luke', 'Jay', 'Rachel', 'Jack']))