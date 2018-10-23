#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: autmanli
@license: Apache Licence
@file: class_unique.py
@time: 2018/10/12 15:47
"""

# 快速排序，使用递归的方法。L：数组；left：左边的下标；right：右边的下标
def quick_sort(array, left, right):
    # 当left=right结束
    if left < right:
        # 取到q的位置，快速排序每次都能得到一个元素的位置
        q = partition(array, left, right)
        # 递归该位置前面的数，即比q小的数
        quick_sort(array, left, q - 1)
        # 递归该位置后面的数，即比q大的数
        quick_sort(array, q + 1, right)

# 取最左边的数为基准数，将比它大的放左边，比它小的放右边，找到它的位置
def partition(array, left, right):
    key = array[left]
    while left < right:
        # 如果array[right]>=key 就不交换位置，right-1
        while left < right and array[right] >= key:
            right -= 1
        # 如果array[right]<key 将array[right]放置到array[left]，left+1
        while left < right and array[right] < key:
            array[left] = array[right]
            left += 1
            # 查找array下一个位置
            array[right] = array[left]

    #将基准数放置到该位置
    array[left] = key
    return left

#直接插入排序
def insertSort(array):
    # 获取列表长度
    length=len(array)
    for i in range(1, length):
        j = i - 1
        # 如果当前值小于前一个元素,则将当前值作为一个临时变量存储,将前一个元素后移一位
        if (array[i] < array[j]):
            temp = array[i]
            array[i] = array[j]

            # 继续往前寻找,如果有比临时变量大的数字,则后移一位,直到找到比临时变量小的元素或者达到列表第一个元素
            j = j - 1
            while j >= 0 and array[j] > temp:
                array[j + 1] = array[j]
                j = j - 1

            # 将临时变量赋值给合适位置
            array[j + 1] = temp




L=[100,8,20,93,81,29,83,10,12,40,2]
# quick_sort(L,0,len(L)-1)
# print(L)

insertSort(L)
print(L)



