# SESSDSA18课程上机作业
# 【H9】排序查找编程作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中的函数体内编写代码，每个题目的函数后有调用语句用于检验
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业在5月25日23：59之前提交到作业提交网站

# 划重点：
#### 将本文件与一个说明分析文档共两个文件打包提交，
#### 命名为h9_学号_姓名，如h9_1700000012_张三

#
# by TYY
# 2018.5.15

# =========== 1 无切片的二分搜索 ==========
# 用递归算法实现二分搜索，避免用切片操作。

def binarySearch_noSlice(alist, item):
    def biSearch(alist, item, start, end):                      # 一个记录搜索部分列表头尾的函数
        if start > end:                                         # 最后未找到该元素
            return False
        mid = (start+end)//2
        if alist[mid] == item:                                  # 在某次取中值时找到该元素
            return True
        elif alist[mid] < item:
            return biSearch(alist, item, mid+1, end)            # 递归，找后半部分，或line31找前半部分
        else:
            return biSearch(alist, item, start, mid-1)
    return biSearch(alist, item, 0, len(alist)-1)


# 检验
print(binarySearch_noSlice([1, 2, 3, 4, 5], 5))                                                     # True
print(binarySearch_noSlice([1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97], 70)) # False
print(binarySearch_noSlice([1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100, 109, 118, 127, 136, 145, 154, 163, 172, 181, 190, 199, 208, 217,
       226, 235, 244, 253, 262, 271, 280, 289, 298], 233))                                          # False


# =========== 2 ADT Map =================
# 采用数据链(chaining)的冲突解决技术来实现ADT Map，
# 要求实现ADT Map中定义的所有方法：put(key, data), get(key), __delitem__(key), __len(), __contains__(key)

class HashMap_chaining():
    def __init__(self, size=11):
        self.length = 0                                     # 维护map的变量length储存已储存的数据数目，和槽数目size
        self.size = size
        self.keys = [[] for i in range(size)]               # 每个槽为一个列表，且key和value分开
        self.datas = [[] for i in range(size)]

    def put(self, key, data):
        index = key % self.size
        if key in self.keys[index]:                         # 如果已经有该key，重新赋值
            i = self.keys[index].index(key)
            self.datas[index][i] = data
        else:                                               # 没有key，新增键值对
            self.keys[index].append(key)
            self.datas[index].append(data)
            self.length += 1

    def get(self, key):
        i = self.keys[key % self.size].index(key)
        return self.datas[key % self.size][i]

    __setitem__ = put
    __getitem__ = get

    def __delitem__(self, key):
        i = self.keys[key % self.size].index(key)           # 在槽列表中找到key的位置，而后删除
        del self.keys[key % self.size][i]
        del self.datas[key % self.size][i]
        self.length -= 1

    def __len__(self):
        return self.length

    def __contains__(self, key):
        return key in self.keys[key % self.size]


# 检验
m = HashMap_chaining()
for i in range(1, 101, 11):
    m[i] = i
print(len(m))
for i in range(1, 101, 22):
    print(m[i], end=' ')
print()
for i in range(1, 101, 22):
    m[i] = i * 2
for i in range(1, 101, 11):
    print(m[i], end=' ')
print()
for i in range(1, 101, 22):
    del m[i]
print(len(m))
for i in range(1, 101, 11):
    print(i in m, end=' ')
print()

# 10
# 1 23 45 67 89
# 2 12 46 34 90 56 134 78 178 100
# 5
# False True False True False True False True False True


# =========== 3 大小自动增长的散列表 =======
# 采用开放定址冲突解决技术的散列表，课件中是固定大小的，如果希望在负载因子达到某个阈值之后，
# 散列表的大小能自动增长，该如何设计算法？
# 请写一个算法说明和分析，并实现之。
class HashTable:
    def __init__(self):
        self.length = 0
        self.size = 11                                              # 初始化槽数为11
        self.datas = [None]*11

    def put(self, data):
        if (self.length+1)/self.size > 0.7:                         # 若添加数据后负载>0.7则扩充槽数到原来两倍
            datalist = [item for item in self.datas if item]        # 取出现有数据
            self.size *= 2
            self.datas = [None]*self.size
            self.length = 0
            for item in datalist:
                self.put(item)                                      # 循环把原数据加入到更大的散列表中
        index = data % self.size
        while self.datas[index]:
            if self.datas[index] == data:                           # 原来数据已存有：跳过
                break
            index = (index+3) % self.size                           # 遇到冲突时再散列：+3线性探测
        else:
            self.datas[index] = data
            self.length += 1

    def __contains__(self, data):
        index = data % self.size
        while self.datas[index] is not None:                        # 查找方式：+3线性探测，直到遇到数据或者None
            if self.datas[index] == data:
                return True
            index = (index+3) % self.size
        return False

    def __len__(self):
        return self.length


# 测试HashTable的代码，添加数据并print出当前散列表的槽数和数据量
h = HashTable()
for i in [1, 11, 8]:
    h.put(i)
print(h.datas)
print(h.size, len(h))
for i in [22, 48, 33, 45]:
    h.put(i)
print(h.datas)
print(h.size, len(h))
for i in [21, 54, 81, 55, 3]:
    h.put(i)
print(h.datas)
print(h.size, len(h))
print(21 in h, 47 in h)
for i in range(20):
    h.put(i)
print(h.datas)
print(h.size, len(h))


# =========== 4 取“中值”快排 ==============
# 自行设计一种取“中值”的方法实现快速排序，并与课件中的快速排序比较性能。
# 请写一个算法说明和分析，并实现之。

# 选取中值的快速排序(五点取样法)
def quickSort(alist):
    def myqsort(alist, start, end):
        if start < end:
            middic = {alist[start]: start, alist[end]: end, alist[(start+end)//2]: (start+end)//2,
                      alist[(start*3+end)//4]: (start*3+end)//4, alist[(start+end*3)//4]: (start+end*3)//4}     # 找中值的方法：五点取样法
            medi = middic[sorted(middic)[len(middic)//2]]                                                       # 从五点(可能不到5点)中找到中值
            left, right = start, end
            while left < right:                                                     # 左右游标的相向移动，直到右游标到左边
                while alist[left] <= alist[medi] and left < end:
                    left += 1
                while alist[right] >= alist[medi] and right > start:
                    right -= 1
                if left < right:
                    alist[left], alist[right] = alist[right], alist[left]           # 遇到左标与右标应该互换
            turn = right if right > medi else left if left < medi else medi         # 最后中值应与哪个游标换位
            alist[medi], alist[turn] = alist[turn], alist[medi]
            myqsort(alist, start, turn-1)                                           # 递归，中值左右两子列的排序
            myqsort(alist, turn+1, end)
    myqsort(alist, 0, len(alist)-1)


# 课本的快速排序，取第一个值为中值
def textQSort(alist):
    def qsort(alist, start, end):
        if start < end:
            left, right = start+1, end                                              # 对第一个值后的数进行游标移动，原理类似上算法
            while left <= right:
                while left <= end and alist[left] <= alist[start]:
                    left += 1
                while right >= start+1 and alist[right] >= alist[start]:
                    right -= 1
                if left < right:
                    alist[left], alist[right] = alist[right], alist[left]
            alist[start], alist[right] = alist[right], alist[start]
            qsort(alist, start, right-1)
            qsort(alist, right+1, end)
    qsort(alist, 0, len(alist)-1)


# 测试两代码用时的代码
from random import shuffle,randrange
from copy import deepcopy
from timeit import Timer
# 以下是对无序性较高的列表进行排序
exp = 4
while exp < 6.5:
    lista = list(range(int(10**exp)))
    shuffle(lista)                                                              # 使用shuffle函数打乱，基本认为很乱
    listb = deepcopy(lista)
    tmra = Timer('quickSort(lista)', 'from __main__ import quickSort, lista')
    tmrb = Timer('textQSort(listb)', 'from __main__ import textQSort, listb')
    timea = tmra.timeit(1)
    timeb = tmrb.timeit(1)
    print('%d\t%.5f\t%.5f' % (int(10**exp), timea, timeb))
    exp += 0.1
# 以下对有一定顺序的列表排序
for length in range(10**4, 25*10**4, 10**4):
    lista = [randrange(i, i+10**4) for i in range(length)]                      # 用randrange构造列表，列表越后项数值大的概率更高
    listb = deepcopy(lista)
    tmra = Timer('quickSort(lista)', 'from __main__ import quickSort, lista')
    tmrb = Timer('textQSort(listb)', 'from __main__ import textQSort, listb')
    timea = tmra.timeit(1)
    timeb = tmrb.timeit(1)
    print('%d\t%.5f\t%.5f' % (length, timea, timeb))

