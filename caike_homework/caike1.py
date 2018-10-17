# -*- coding: utf-8 -*-
def q(alist,start,end):
    #递归终止条件
    if start >=end:
        return
    #low为序列左边移动的游标
    low=start
    #las为序列右边移动的游标
    last=end
    #起始元素设为基准元素
    mid_num=alist[start]
    #循环条件为low和last未重合
    while low<last:
        #右边比较比基准元素大时，将游标向左移动一位
        while low<last and alist[last]>=mid_num:
            last-=1
        #如果比基准小，跳出循环，把该元素放在基准元素左边
        alist[low]=alist[last]
        #左边比较比基准元素小时，将游标向右移动一位
        while low<last and alist[low]<mid_num:
            low+=1
        #如果比基准大，跳出循环，把该元素放在基准元素右边  
        alist[last]=alist[low]
    #当low与last相等，就是mid_num的排序位置
    alist[low]=mid_num
    #对排序好的元素左右两边的序列进行递归
    q(alist,start,low-1)
    q(alist,low+1,end)
    
if __name__=="__main__":
    alist=[30,40,60,10,20,50]
    print(alist)
    q(alist,0,len(alist)-1)
    print(alist)
