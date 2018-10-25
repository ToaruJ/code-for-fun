# SESSDSA18课程上机作业
# 【H6】线性表与链式存储结构编程作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中的函数体内编写代码，每个题目的函数后有调用语句用于检验，
# 上交作业时提交本文件，命名为h6_学号_姓名.py，如h6_1700000012_张三.py
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业在4月10日23：59之前提交到教学网
#
#
# by TYY&ZHD
# 2018.4.2


class Node():
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev

# ======== 1 UnorderedList ========
# 用链表实现UnorderedList的如下方法：isEmpty, add, search, size, remove, append，index，pop，insert, __len__, __getitem__
# 用于列表字符串表示的__str__方法 (注：__str__里不要使用str(), 用repr()代替
# 用于切片的__getitem__方法
# 选做：UnorderedList(iterable) -> new UnorderedList initialized from iterable's items
# 选做：__eq__, __iter__
class UnorderedList():
    def __init__(self, argv=None):
        self.head=self.tail=None       #有头结点和尾结点
        if not argv is None:           #argv是可迭代对象，取每一个元素放入节点中
            for item in argv:
                self.append(item)

    def isEmpty(self):
        return self.head==None

    def add(self, item):
        newnode=Node(item)
        newnode.setNext(self.head)
        self.head=newnode
        if self.tail==None:            #结点加在头部，并维护尾结点(如果原链表为空)
            self.tail=newnode
    
    def search(self, item):
        current=self.head
        while current!=None:
            if current.getData()==item:
                return True
            else:
                current=current.getNext()
        return False

    def size(self):
        count=0
        current=self.head
        while current!=None:
            count+=1
            current=current.getNext()
        return count

    def remove(self, item):
        current=self.head
        prev=None                              #记录当前结点和上一结点
        while current!=None:
            if current.getData()==item:
                if prev==None:                 #对删除位置在头尾时的维护
                    self.head=current.getNext()
                else:
                    prev.setNext(current.getNext())
                if current.getNext()==None:
                    self.tail=prev
                del current
                break
            else:
                prev=current
                current=current.getNext()

    def append(self, item):
        newnode=Node(item)
        if self.tail!=None:                  #判断原链表是否空，若空则要维护头结点
            self.tail.setNext(newnode)
        else:
            self.head=newnode
        self.tail=newnode

    # 搜索value，从下标start到stop，左闭右开
    def index(self, value, start=0, stop=None):
        if stop is None:
            stop = self.size()
        else:
            stop%=self.size()                  #对stop输入负值的处理
        current=self.head
        for i in range(start):                 #移到开始搜索处
            current=current.getNext()
        for i in range(start,stop):
            if current.getData()==value:
                return i
            else:
                current=current.getNext()
        return None

    def pop(self, pos=-1):
        pos%=self.size()                       #对pos是负数的处理
        prev=self.head                         #记录的是要取出结点的前一个
        for index in range(pos-1):
            prev=prev.getNext()
        if pos==0:                             #链表结构改变，并维护头尾结点
            current=prev
            self.head=current.getNext()
        else:
            current=prev.getNext()
            prev.setNext(current.getNext())
        if current.getNext()==None:
            self.tail=prev
        data=current.getData()
        del current
        return data

    def insert(self, pos, item):
        if self.head==None:                  #对空链表的特殊处理
            newnode=Node(item)
            self.head=self.tail=newnode
        else:
            pos%=self.size()+1                 #对pos是负数的处理
            prev=self.head
            for index in range(pos-1):
                prev=prev.getNext()
            newnode=Node(item)
            if pos==0:
                next=prev                      #新结点插入在prev和next中间
                self.head=newnode
            else:
                next=prev.getNext()
                prev.setNext(newnode)
            if next==None:
                self.tail=newnode
            newnode.setNext(next)

    def __len__(self):
        return self.size()

    def __str__(self):
        lst=[]
        current=self.head
        while current!=None:
            lst.append(current.getData())
            current=current.getNext()
        return repr(lst)

    __repr__ = __str__

    def __getitem__(self, argv):
        #请参考：http://gis4g.pku.edu.cn/python3-slice-getitem/
        #可以不用处理负数
        current=self.head
        if isinstance(argv,int):                   #给入整数，返回其内容
            for index in range(argv):
                current=current.getNext()
            return current.getData()
        elif isinstance(argv,slice):               #给入切片，返回新链表
            newlst=UnorderedList()
            if argv.start==None:                   #对切片argv某些参数是None的处理
                start=0
            else:
                start=argv.start
            if argv.stop==None:
                stop=self.size()
            else:
                stop=argv.stop
            if argv.step==None:
                step=1
            else:
                step=argv.step
            cnt=0
            for index in range(start):
                current=current.getNext()
            for index in range(start,stop):        #取出原链表的切片，按step跳过
                if cnt%step==0:
                    newlst.append(current.getData())
                cnt+=1
                current=current.getNext()
            return newlst

    def __eq__(self,other):
        selft,othert=self.head,other.head
        while selft!=None and othert!=None:         #对两个链表元素逐一比较
            if selft.getData()!=othert.getData():
                return False
            else:
                selft=selft.getNext()
                othert=othert.getNext()
        return selft==None and othert==None         #最后链表长度相等才算两者相等

    def __iter__(self):
        self.current=self.head
        return self                                 #返回自身迭代器，并设置current位置记录当前迭代位置
                                                    #__next__方法来取出下一个迭代对象
    def __next__(self):
        if self.current!=None:
            data=self.current.getData()
            self.current=self.current.getNext()
            return data
        else:
            del self.current
            raise StopIteration()

# 检验
print("======== 1 UnorderedList ========")
mylist = UnorderedList()
for i in range(0, 20, 2):
    mylist.append(i)
mylist.add(3)
mylist.remove(6)
print(mylist.isEmpty())           # False
print(mylist.search(5))           # False
print(mylist.size())              # 10
print(mylist.index(2))            # 2
print(mylist.pop())               # 18
print(mylist.pop(2))              # 2
print(mylist)                     # [3, 0, 4, 8, 10, 12, 14, 16]
mylist.insert(3, "10")
print(len(mylist))                # 9
print(mylist[4])                  # 8
print(mylist[3:8:2])              # ['10', 10, 14]

# ======== 2 OrderedList ========
# 将OrderedList作为UnorderedList的子类来实现
# 实现ADT OrderedList的所有接口:
# add, remove, search, isEmpty, size, index, pop
# 注：不继承insert, append方法
class OrderedList(UnorderedList):
    def __init__(self, argv=None):
        if argv is None:
            super().__init__()
        else:
            super().__init__(sorted(argv))

    def add(self, item):
        newnode=Node(item)
        next=self.head
        prev=None
        while next!=None and item>=next.getData(): #找到应该插入的位置
            prev=next
            next=next.getNext()
        if prev==None:
            self.head=newnode
        else:
            prev.setNext(newnode)
        newnode.setNext(next)

    def search(self, item):
        current=self.head
        while current!=None and current.getData()<=item:
            if current.getData()==item:
                return True
            else:
                current=current.getNext()
        return False

    def index(self, value, start=0, stop=None):
        if stop is None:
            stop = self.size()
        else:
            stop%=self.size()                  #对stop输入负值的处理
        current=self.head
        for i in range(start):                 #移到开始搜索处
            current=current.getNext()
        for i in range(start,stop):
            if current.getData()==value:
                return i
            elif current.getData()>value:
                break
            else:
                current=current.getNext()
        return None

    def __getitem__(self, argv):
        part=super().__getitem__(argv)         #运用父类的切片操作，并转换类型
        if isinstance(part,UnorderedList):
            return OrderedList(part)
        else:
            return part
            
    def insert(self,pos,item):
        pass
     
    def append(self,item):
        pass

# 检验
print("======== 2 OrderedList ========")
mylist = OrderedList()
for i in range(0, 10, 2):
    mylist.add(i)
mylist.add(3)
mylist.remove(6)
mylist.add(5)
print(mylist.isEmpty())         # False
print(mylist.search(8))         # True
print(mylist)                   # [0, 2, 3, 4, 5, 8]
print(mylist.pop())             # 8
print(mylist.size())            # 5
print(mylist.index(4))          # 3
print(mylist.pop(-2))           # 4
print(mylist[1:])               # [2, 3, 5]



# ======== 3 ADT Stack & Queue ========
# 用链表实现ADT Stack与ADT Queue的所有接口
class Stack():
    def __init__(self):
        self.head=None                         #定义头结点，头结点处栈顶

    def isEmpty(self):
        return self.head==None

    def push(self,item):
        newnode=Node(item)
        newnode.setNext(self.head)
        self.head=newnode

    def pop(self):
        delnode=self.head
        data=delnode.getData()
        self.head=delnode.getNext()
        del delnode
        return data

    def peek(self):
        return self.head.getData()

    def size(self):
        count=0
        current=self.head
        while current!=None:
            count+=1
            current=current.getNext()
        return count

class Queue():
    def __init__(self):
        self.head=self.tail=None          #链表head为队首，tail为队尾

    def isEmpty(self):
        return self.head==None

    def enqueue(self,item):
        newnode=Node(item)
        if self.head==None:               #原队列为空的处理
            self.head=self.tail=newnode
        else:
            self.tail.setNext(newnode)
            self.tail=newnode

    def dequeue(self):
        delnode=self.head                 #delnode结点出列
        data=delnode.getData()
        self.head=delnode.getNext()
        del delnode
        if self.head==None:               #原队列为空的处理
            self.tail=None
        return data

    def size(self):
        count=0
        current=self.head
        while current!=None:
            count+=1
            current=current.getNext()
        return count


# 检验
print("======== 3 ADT Stack & Queue ========")
s = Stack()
q = Queue()
for i in range(10):
    s.push(i)
    q.enqueue(i)
print(s.peek(), q.dequeue())      # 9 0
print(s.pop(), q.size())          # 9 9
while not s.isEmpty():
    s.pop()
print(s.size(), q.isEmpty())      # 0 False



# ======== 4 DoublyLinkedList ========
# 实现双向链表版本的UnorderedList，接口同ADT UnorderedList
# 在节点Node中增加prev变量，引用前一个节点
# 在UnorderedList中增加tail变量，引用列表中最后一个节点
# 增加getTail方法
class DoublyLinkedList():
    def __init__(self, argv=None):
        self.head=self.tail=None     #有头结点和尾结点
        if not argv is None:         #argv是可迭代对象，取每一个元素放入节点中
            for item in argv:
                self.append(item)

    def isEmpty(self):
        return self.head==None

    def getTail(self):
        return self.tail

    def add(self, item):
        newnode=Node(item)
        newnode.setNext(self.head)
        if self.tail==None:            #结点加在头部，并维护尾结点(如果原链表为空)
            self.tail=newnode
        else:
            self.head.setPrev(newnode)
        self.head=newnode
    
    def search(self, item):
        current=self.head
        while current!=None:
            if current.getData()==item:
                return True
            else:
                current=current.getNext()
        return False

    def size(self):
        count=0
        current=self.head
        while current!=None:
            count+=1
            current=current.getNext()
        return count

    def remove(self, item):
        current=self.head
        while current!=None:
            if current.getData()==item:
                if current.getPrev()==None:                 #对删除位置在头尾时的维护
                    self.head=current.getNext()
                else:
                    current.getPrev().setNext(current.getNext())
                if current.getNext()==None:
                    self.tail=current.getPrev()
                else:
                    current.getNext().setPrev(current.getPrev())
                del current
                break
            else:
                current=current.getNext()

    def append(self, item):
        newnode=Node(item)
        if self.tail!=None:                    #判断原链表是否空，若空则要维护头结点
            self.tail.setNext(newnode)
            newnode.setPrev(self.tail)
        else:
            self.head=newnode
        self.tail=newnode

    def index(self, value, start=0, stop=None):
        if stop is None:
            stop = self.size()
        else:
            stop%=self.size()                  #对stop输入负值的处理
        current=self.head
        for i in range(start):                 #移到开始搜索处
            current=current.getNext()
        for i in range(start,stop):
            if current.getData()==value:
                return i
            else:
                current=current.getNext()
        return None

    def pop(self, pos=-1):
        if pos>=0:                             #根据pos正负设置起始处和迭代函数
            current=self.head
            get=Node.getNext
        else:
            current=self.tail
            get=Node.getPrev
            pos=-(pos+1)
        pos%=self.size()                       #对pos给入非常规值，轮回方式取位置
        while pos>0:
            current=get(current)
            pos-=1
        if current.getNext()==None:            #对pop结点在头尾的处理
            self.tail=current.getPrev()
        else:
            current.getNext().setPrev(current.getPrev())
        if current.getPrev()==None:
            self.head=current.getNext()
        else:
            current.getPrev().setNext(current.getNext())
        data=current.getData()
        del current
        return data

    def insert(self, pos, item):
        newnode=Node(item)
        if pos>=0:                             #根据pos正负设置起始处和索引方向
            next=self.head                     #重命名根据索引方向的函数，getn，setn是索引方向下一个
            getn=Node.getNext
            getp=Node.getPrev
            setn=Node.setNext
            setp=Node.setPrev
            turn=False
        else:
            next=self.tail
            getn=Node.getPrev
            getp=Node.getNext
            setn=Node.setPrev
            setp=Node.setNext
            pos=-(pos+1)
            turn=True
        prev=None                              #插入位点在prev和next中间
        while pos>0 and next!=None:
            prev=next
            next=getn(next)
            pos-=1
        if next==None:                         #对于插入处在链表头尾与否的不同处理
            if turn:
                self.head=newnode
            else:
                self.tail=newnode
        else:
            setp(next,newnode)
            setn(newnode,next)
        if prev==None:
            if turn:
                self.tail=newnode
            else:
                self.head=newnode
        else:
            setn(prev,newnode)
            setp(newnode,prev)

    def __len__(self):
        return self.size()

    def __str__(self):
        lst=[]
        current=self.head
        while current!=None:
            lst.append(current.getData())
            current=current.getNext()
        return repr(lst)

    __repr__ = __str__

    def __getitem__(self, argv):
        if isinstance(argv,int):                   #给入整数，返回其内容
            if argv>=0:                            #根据argv正负确定索引方向
                current=self.head
                get=Node.getNext
            else:
                current=self.tail
                get=Node.getPrev
                argv=-(argv+1)
            argv%=self.size()
            for index in range(argv):
                current=get(current)
            return current.getData()
        elif isinstance(argv,slice):               #给入切片，返回新链表
            current=self.head
            newlst=DoublyLinkedList()
            if argv.start==None:                   #对切片argv某些参数是None的处理
                start=0
            else:
                start=argv.start
            if argv.stop==None:
                stop=self.size()
            else:
                stop=argv.stop
            if argv.step==None:
                step=1
            else:
                step=argv.step
            cnt=0
            for index in range(start):             #到达切片起始处
                current=current.getNext()
            for index in range(start,stop):        #取出原链表的切片，按step跳过
                if cnt%step==0:
                    newlst.append(current.getData())
                cnt+=1
                current=current.getNext()
            return newlst

    def __eq__(self,other):
        selft,othert=self.head,other.head
        while selft!=None and othert!=None:         #对两个链表元素逐一比较
            if selft.getData()!=othert.getData():
                return False
            else:
                selft=selft.getNext()
                othert=othert.getNext()
        return selft==None and othert==None         #最后链表长度相等才算两者相等

    def __iter__(self):
        self.current=self.head
        return self                                 #返回自身迭代器，并设置current位置记录当前迭代位置
                                                    #__next__方法来取出下一个迭代对象
    def __next__(self):
        if self.current!=None:
            data=self.current.getData()
            self.current=self.current.getNext()
            return data
        else:
            del self.current
            raise StopIteration()


# 检验
print("======== 4 DoublyLinkedList ========")
mylist = DoublyLinkedList()
for i in range(0, 20, 2):
    mylist.append(i)
mylist.add(3)
mylist.remove(6)
print(mylist.getTail().getPrev().getData())   # 16
print(mylist.isEmpty())                       # False
print(mylist.search(5))                       # False
print(mylist.size())                          # 10
print(mylist.index(2))                        # 2
print(mylist.pop())                           # 18
print(mylist.pop(2))                          # 2
print(mylist)                                 # [3, 0, 4, 8, 10, 12, 14, 16]
mylist.insert(3, "10")
print(len(mylist))                            # 9
print(mylist[4])                              # 8
print(mylist[3:8:2])                          # ['10', 10, 14]
