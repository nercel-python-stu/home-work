#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: autmanli
@license: Apache Licence 
@file: class_unique.py
@time: 2018/10/12 15:47
"""

class uniqueClass(object):
    def __new__(cls, *args, **kwargs):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(uniqueClass, cls).__new__(cls)
        return cls.instance

obj1=uniqueClass()
obj2=uniqueClass()
print(obj1==obj2)

class Singleton2(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(Singleton2,self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton2,self).__call__(*args, **kwargs)
        return self.__instance


class Foo(object):
    __metaclass__ = Singleton2 #在代码执行到这里的时候，元类中的__new__方法和__init__方法其实已经被执行了，而不是在Foo实例化的时候执行。且仅会执行一次。


foo1 = Foo()
foo2 = Foo()
print (Foo.__dict__)  #_Singleton__instance': <__main__.Foo object at 0x100c52f10> 存在一个私有属性来保存属性，而不会污染Foo类（其实还是会污染，只是无法直接通过__instance属性访问）

print (foo1 is foo2)  # True