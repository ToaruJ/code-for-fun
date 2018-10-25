'''
SESSDSA18课程上机作业
【H2】Python入门编程

说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
（1）直接在本文件中的函数体内编写代码，每个题目的函数后有调用语句用于检验，
上交作业时提交本文件，命名为h2_学号_姓名.py，如h2_1700000012_张三.py
（2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
（3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
（4）作业在3月16日 23：59之前提交到教学网


by TYY
2018.3.9
'''



'''
======= 1 字符移动 =======
创建一个函数，接受一个字符串和一个正整数n作为参数，
返回把原字符串字符位置向右移动n个字符的字符串。
例如：
** 接受的参数是"abcd"和1，返回的字符串是"dabc"；
** 接受的参数是"mnbol"和2，返回的字符串是"olmnb"。
'''
def reverse(s, n):
    result = ""
    # 请在此写下你的代码
    n%=len(s)             #防止出现n>len(s)的情况
    result=s[-n:]+s[:-n]
    # 代码结束
    return result

# 调用检验
print("1-reverse", reverse("abcd", 1))
print("1-reverse", reverse("mnbol", 2))


'''
======= 2 阶乘求和 =======
创建一个函数，接受一个正整数n作为参数，返回s=1!+2!+3!+……+n!的值。
例如：
** 接受的参数是3，返回的数是9；
** 接受的参数是6，返回的数是873。
'''
def factorailSum(n):
    s = 0
    # 请在此写下你的代码
    p=1                   # p是当前循环阶乘的结果
    for i in range(1,n+1):
        p*=i
        s+=p
    # 代码结束
    return s

# 调用检验
print("2-factorailSum", factorailSum(3))
print("2-factorailSum", factorailSum(6))


'''
======= 3 数字转换 =======
创建一个函数，接受一个英文字符串作为参数，返回该字符串的整数表示。
例如：
** 接受的参数是"eight-nine"，返回的是89；
** 接受的参数是"one-two-three-four-five"，返回的是12345。
'''
def transNum(s):
    n = 0
    # 请在此写下你的代码
    dic=dict(zip(["zero","one","two","three","four",
    	"five","six","seven","eight","nine"],range(10)))
    lst=s.split('-')
    for item in lst:      #数位累加法
        n=n*10+dic[item]
    # 代码结束
    return n

# 调用检验
print("3-transNum", transNum("eight-nine"))
print("3-transNum", transNum("one-two-three-four-five"))


'''
======= 4 创建字典 =======
创建一个函数，接受两个长度相同的元组，
用这两个元组中的所有数据组成一个字典并返回。
例如：
** 接受的参数是(1, 2, 3)和("abc", "def", "ghi")，返回{1:"abc", 2:"def", 3:"ghi"}。
'''
def createDict(keys, values):
    d = dict()
    # 请在此写下你的代码
    d=dict(zip(keys,values))
    # 代码结束
    return d

# 调用检验
print("4-creatDict", createDict((1,2,3), ("abc","def","ghi")))


'''
======= 5 创建集合 =======
创建一个函数，接受两个字符串作为参数，返回两个字符串字符集合的并集。
例如：
** 接受的参数为"abc"和"bcd"，返回set(['a', 'b', 'c', 'd'])。
'''
def createSet(s1, s2):
    union = set()
    # 请在此写下你的代码
    union=set(s1)|set(s2)
    # 代码结束
    return union

# 调用检验
print("5-creatSet", createSet("abc", "bcd"))


'''
======= 6 月份天数 =======
创建一个函数，接受两个参数y和m，分别表示年和月，返回此年此月的天数。
（如大月有31天，小月有30天，而闰年的2月有29天，平年则只有28天，
年份如果能被4整除但不能被100整除或者能被400整除为闰年）
例如：
** 接受的参数为2018和2，返回28
** 接受的参数为2015和7，返回31
'''
def countDays(y, m):
    day = 0
    # 请在此写下你的代码
    bigm={1,3,5,7,8,10,12}
    smallm={4,6,9,11}      #定义大月小月
    if m in bigm:
        day=31
    elif m in smallm:
        day=30
    else:                  #单独对二月
        if y%400==0:
            day=29
        elif y%100==0:
            day=28
        elif y%4==0:
            day=29
        else:
            day=28
    # 代码结束 
    return day

# 调用检验
print("6-countDays", countDays(2018, 2))
print("6-countDays", countDays(2015, 7))


'''
======= 7 判断水仙花数 =======
创建一个函数，接受一个参数n(n>=100)，判断这个数是否为水仙花数，
返回True或者False。（即满足如果这个数为m位数，
则每个位上的数字的m次幂之和等于它本身。）
例如：
** 接受参数为153，返回True（1^3 + 5^3+ 3^3 = 153）
** 接受参数为282，返回False
'''
def isNarcNum(n):
    flag = False
    # 请在此写下你的代码
    lst=list(str(n))  #将数字分开
    m=len(lst)
    s=0               #幂的和值
    for num in lst:
        s+=int(num)**m
    if n==s:
        flag=True
    # 代码结束
    return flag

# 调用检验
print("7-isNarcNum", isNarcNum(153))
print("7-isNarcNum", isNarcNum(282))


'''
======= 8 杨辉三角 =======
创建一个函数，接受一个参数n，返回n阶杨辉三角。
例如：
** 接受参数为6，返回：
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
'''
def printTri(n):
    s = ""
    # 请在此写下你的代码
    nlst=[['1']]           #用嵌套列表储存数值
    s+="1"
    for i in range(1,n):
        nlst.append(['1'])
        for j in range(i-1):
            nlst[i].append(str(int(nlst[i-1][j])
            	+int(nlst[i-1][j+1])))
        nlst[i].append('1')
        s+='\n'+' '.join(nlst[i])
    # 代码结束
    return s

# 调用检验
print("8-printTri", printTri(6),sep='\n')


'''
======= 9 判断质数 =======
对于大于1的数，如果除了1和它本身，它不能再被其它正整数整除，
那么我们说它是一个质数。创建一个函数，接受一个参数n，判断它是否是质数。
例如：
** 接受参数为18，返回False
** 接受参数为31，返回True
'''
def isPrime(n):
    flag = False
    # 请在此写下你的代码
    i=2               #测试因数
    while i**2<=n:
        if n%i==0:
            break
        i+=1
    else:
        flag=True
    # 代码结束
    return flag

# 调用检验
print("9-isPrime", isPrime(18))
print("9-isPrime", isPrime(31))


'''
======= 10 水仙花数 =======
创建一个函数，接受一个参数max(max>=1000)，调用另一题编写的判断函数，
求100到max之间的水仙花数，返回一个包含换行符的字符串，
每个数作为一行输出（每一个数之后有一个换行符'\n'，包括最后一个数）
例如：
** 接受参数为2333，返回：
153
370
371
407
1634
'''
def printNarcNum(n):
    s = ""
    # 请在此写下你的代码
    for i in range(100,n):
        if isNarcNum(i):
            s+='\n'+str(i)
    # 代码结束
    return s

# 调用检验
print("10-printNarcNum",printNarcNum(2333))

