from timeit import Timer
from random import randrange
from androidhelper import Android

droid=Android()
droid.dialogCreateAlert('H4 start',
	'press Yes to start H4, press No to exit')
droid.dialogSetPositiveButtonText('Yes')
droid.dialogSetNegativeButtonText('No')
droid.dialogShow()
if droid.dialogGetResponse().result['which']=='positive':
#打开储存结果文件
    ftxt=open('/storage/emulated/0/qpython/result.txt','w')
    
    print('process H4.1')
#H4.1 测量不同大小的list索引取值用时
    ftxt.write('H4.1 list index time\nlen(list)  time\n')
    droid.dialogCreateHorizontalProgress('H4.1 progress',
    	'H4.1 is now testing',30)
    droid.dialogShow()
    for nlen in range(10**5,3*10**6+1,10**5):
        lst=list(range(nlen))
        tmr=Timer('lst[10000]','from __main__ import lst')
        t=tmr.timeit(number=5*10**6)
        ftxt.write('%d %.5f\n'%(nlen,t))
        droid.dialogSetCurrentProgress(nlen//10**5)
    droid.dialogDismiss()
    droid.makeToast('H4.1 finish!')
    
    print('process H4.2')
#H4.2 测量不同大小dict的取值&改值用时
    ftxt.write('\nH4.2 time of dict index and set value\n')
    ftxt.write('len(dict) index_time set_time\n')
    droid.dialogCreateHorizontalProgress('H4.2 progress',
    	'H4.2 is now testing',30)
    droid.dialogShow()
    for nlen in range(10**5,3*10**6+1,10**5):
        dic={x:x for x in range(nlen)}
        tmri=Timer('dic[10000]','from __main__ import dic')
        ti=tmri.timeit(number=3*10**6)
        tmrs=Timer('dic[10000]=20','from __main__ import dic')
        ts=tmrs.timeit(number=3*10**6)
        ftxt.write('%d %.5f %.5f\n'%(nlen,ti,ts))
        droid.dialogSetCurrentProgress(nlen//10**5)
    droid.dialogDismiss()
    droid.makeToast('H4.2 finish!')
    
    print('process H4.3')
#H4.3 测量不同大小list和dict的del函数用时
    ftxt.write('\nH4.3 time of delete item of list and dict\n')
    ftxt.write('len()  list_time  dict_time\n')
    droid.dialogCreateHorizontalProgress('H4.3 progress',
    	'H4.3 is now testing',30)
    droid.dialogShow()
    for nlen in range(10**5,3*10**6+1,10**5):
        lst=list(range(nlen))
        dic={x:x for x in range(nlen)}
        #由于lst规模很大，删除部分可忽略不计
        tmrl=Timer('del lst[10000]','from __main__ import lst')
        tl=tmrl.timeit(number=100)
        #由于dic的key值唯一，不可反复删除，只能测量两次操作时间差，减去赋值语句时间
        tmrd=Timer('del dic[10000];dic[10000]=10000',
        	'from __main__ import dic')
        td1=tmrd.timeit(number=100)
        tmrd=Timer('dic[10000]=10000','from __main__ import dic')
        td2=tmrd.timeit(number=100)
        ftxt.write('%d %.5f %.5e\n'%(nlen,tl,td1-td2))
        droid.dialogSetCurrentProgress(nlen//10**5)
    droid.dialogDismiss()
    droid.makeToast('H4.3 finish!')
    
    print('process H4.4')
#H4.4 测量不同大小list取第k小值用时，复杂度O(nlog(n)),O(n)
    #比较排序后取第k小数，复杂度O(nlog(n))
    def get_small_nln(lst,k):
        tlst=sorted(lst)
        return tlst[k-1]
    #计数法，然后从小到大依次取到第k小的数，复杂度O(n)
    def get_small_n(lst,rng,k):
        cntlst=[0]*rng         #存放每个数的出现次数
        for item in lst:
            cntlst[item]+=1
        cnt,i=0,0
        while cnt<k:
            cnt+=cntlst[i]
            i+=1
        return i-1
    #H4.4主程序，测量两种算法用时
    ftxt.write('\nH4.4 time of pick kth smallest item\n')
    ftxt.write('len(lst) nlogn_time n_time\n')
    droid.dialogCreateHorizontalProgress('H4.4 progress',
    	'H4.4 is now testing',30)
    droid.dialogShow()
    for nlen in range(10**4,3*10**5+1,10**4):
        lst=[randrange(10**6) for i in range(nlen)]
        tmrnln=Timer('get_small_nln(lst,1000)',
        	'from __main__ import get_small_nln,lst')
        tnln=tmrnln.timeit(number=2)
        tmrn=Timer('get_small_n(lst,10**6,1000)',
        	'from __main__ import get_small_n,lst')
        tn=tmrn.timeit(number=2)
        ftxt.write('%d %.5f %.5f\n'%(nlen,tnln,tn))
        droid.dialogSetCurrentProgress(nlen//10**4)
    droid.dialogDismiss()
    droid.makeToast('H4.4 finish!')
    
#关闭文件
    ftxt.close()
    droid.dialogCreateAlert('H4 finish',
    	'press OK to exit')
    droid.dialogSetPositiveButtonText('OK')
    droid.dialogShow()

