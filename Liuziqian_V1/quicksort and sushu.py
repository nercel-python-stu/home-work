# -*- coding: utf-8 -*-
def sushu(x):
    amount = 0
    #取从2到x中所有的整数
    for i in range(2,x+1):
        flag=0
        #每个i除以2到i-1的所有数，存在余数为0的情况则为合数，否则为素数
        for j in range(2,i):
            if i/j==0:
                flag=1
        if flag==0:
            print(i)
            amount+=1
    print('%d以内一共有%d个素数'%(x,amount))
        
sushu(100000)            

################算100000以内的素数############################
#快速排序的实现
import random
monitor=0
def Partition(R,low,high):
    #monitor为监视哨
    monitor = R[low]
    pivotkey = R[low] #枢轴记录关键值
    while low<high:     #当high和low值相等时则结束
        while low<high and R[high]>=pivotkey:
            high-=1     #先从后往前查找，若high指向的值大于等于关键值则不进行改变，同时high向前移动
        R[low]=R[high]  #否则将high指向的值赋给low指向的值
        while low<high and R[low]<=pivotkey:
            low+=1      #现在从前往后查找，low指向的值小于关键值则不进行改变，同时low向后移动
        R[high]=R[low]  #否则将low指向的值赋给high指向的值
    R[low]=monitor      #将监视哨的值置于当前的low处，即每次找到待排序位置的第一个值的最终位置
    return low

def Qsort(L,low,high):
    if low<high-1: #长度大于1
        pivotloc=Partition(L,low,high) #将L一分为二
        Qsort(L,low,pivotloc-1)
        Qsort(L,pivotloc+1,high)

#随机产生100个0-100以内的整数，填入列表中，对列表进行快速排序
L_sort=[]
for i in range(0,100):
    L_sort.append(random.randint(0,100))
print(L_sort,'\n')
Qsort(L_sort,0,len(L_sort)-1)
print(L_sort,'\n')
del L_sort[:]

#将0-100倒序填入列表中，并对列表进行快排
for i in range(100,0,-1):
    L_sort.append(i)
print(L_sort,'\n')
Qsort(L_sort,0,len(L_sort)-1)
print(L_sort,'\n')
del L_sort[:]

def quick_sort():
    while True:
        num = input('输入一个待排序整数，输入的不是整数则进行排序:')
        if num.isnumeric()==True:
            L_sort.append(int(num))
            print(L_sort)
        else:
            if len(L_sort)==0:
                print('列表为空，重新输入!',end='')
                continue
            else:
                Qsort(L_sort,0,len(L_sort)-1)
                print(L_sort,'\n')
                del L_sort[:]
                break


    








    
