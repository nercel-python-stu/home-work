# -*- coding: utf-8 -*-
import time
import threading
import re
import random
class Singleton(object):
    _instance_lock = threading.Lock()
    monitor=0

    def __init__(self):
        pass
    
    def is_valid_PhoneNumber(self,Phonenumber):
        phone_pat = re.compile(r'^1[3-9]\d{9}$')
        numbermatch = phone_pat.match(Phonenumber)
        #进行最初的最简单正则匹配
        if numbermatch:
            three = Phonenumber[0:3]
            #print('这是一个正确的手机号',end='')
        
            if(re.match(r'1(3[4-9]|47|5[0-2]|5[7-9]|78|8[2-4]|8[7-8]|98)$',three)):
                #前三位号码进行移动公司号段匹配
                print('这是一个正确的手机号,且为中国移动的号码.')
            
            elif(re.match(r'1(3[0-2]|45|5[5-6]|76|8[5-6])$',three)):
                #前三位号码进行联通公司号段匹配
                print('这是一个正确的手机号,且为中国联通的号码.')
            
            elif(re.match(r'1(33|49|53|73|77|8[0-1]|89|99)$',three)):
                #前三位号码进行电信公司号段匹配
                print('这是一个正确的手机号,且为中国电信的号码.')

            else:
                print('这不是一个正确的手机号!')
        else:
            print('这不是一个正确的手机号!')
            

    def is_valid_email(self,Addr):
        #初步验证邮箱格式是否正确,正确后在函数体内调用is_exist_email()函数判断后缀名是否合法
        if Addr[0]== '<':
            #例如：<Tom Paris> tom@voyager.org
            email_pat = re.compile(r'^(\<)([a-zA-Z\s]+)(\>)(\s?)([0-9a-zA-Z\.\_]+)@([0-9a-zA-Z]+)(.[0-9a-zA-Z\.]+)$')
            #找到@后所表示的邮箱

        else:
            #例如bill.gates@microsoft.com
            email_pat = re.compile(r'^([0-9a-zA-Z\.\_]+)@([0-9a-zA-Z]+)(.[0-9a-zA-Z\.]+)$')
        
        if not email_pat.match(Addr):
            print('这是一个不合法的Email地址！！')
            return
    
        length = len(email_pat.match(Addr).groups())
    
        #调用后缀检查函数
        postfix = email_pat.match(Addr).group(length)
        #通过后缀进一步判断邮箱是否合法
        #将.ccnu.edu.cn这种类型后缀转化成列表,post是一个list
        post = re.split(r'[\.]+', postfix)
        #定义最终匹配规则
        post_pat = re.compile(r'^(ae|net|com|org|cn|sy|tr|ru|edu|zw|co|na|es|uk|vn|il|np|jp|mn|at|mx)$')
        if post_pat.match(post[-1]):
            print('这是一个合法的Email地址，',end='')
            #找到@后所表示的邮箱，例如qq，雅虎，microsoft
            email_name = email_pat.match(Addr).group(length-1)
            print('且这是一个{}的邮箱'.format(email_name))
        else:
            print('这是一个不合法的Email地址！！')


    def Partition(self,R,low,high):
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

    def Qsort(self,L,low,high):
        if low<high-1: #长度大于1
            pivotloc=self.Partition(L,low,high) #将L一分为二
            self.Qsort(L,low,pivotloc-1)
            self.Qsort(L,pivotloc+1,high)

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)  
        return Singleton._instance

obj1 = Singleton()
obj1.is_valid_email('<Tom Paris> tom@voyager.org')
obj1.is_valid_PhoneNumber('13972131700')

#随机产生100个0-100以内的整数，填入列表中，对列表进行快速排序
L_sort=[]
for i in range(0,100):
    L_sort.append(random.randint(0,100))
print(L_sort,'\n')
obj1.Qsort(L_sort,0,len(L_sort)-1)
print(L_sort,'\n')
del L_sort[:]

#将0-100倒序填入列表中，并对列表进行快排
for i in range(100,0,-1):
    L_sort.append(i)
print(L_sort,'\n')
obj1.Qsort(L_sort,0,len(L_sort)-1)
print(L_sort,'\n')
del L_sort[:]

'''
obj2.is_valid_email()
obj2.is_valid_PhoneNumber()
obj3.is_valid_email()
obj3.is_valid_email('<Tom Paris> tom@voyager.org')
obj3.is_valid_email('bill.gates@microsoft.com')
obj3.is_valid_email('tom@voyager.org')
obj3.is_valid_email('chenjy@mail.ccnu.edu.cn')
obj3.is_valid_email('bob#example.com')
obj3.is_valid_email('mr-bob@example.com')
obj3.is_valid_email('someone@gmail.com')
obj3.is_valid_email('tmht@mail.ccnu.edu.cn')
obj3.is_valid_email('epower@mail.ccnu.edu.cn')
obj3.is_valid_email('...@mail...cn')
'''
























