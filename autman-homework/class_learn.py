#!/usr/bin/env python
# encoding: utf-8

import inspect
"""
@version: ??
@author: autmanli
@license: Apache Licence 
@file: class_learn.py
@time: 2018/10/12 10:04
"""

class A(object):
    pass


class B(A):
    pass

class C(B):
    pass

class D(B):
    pass

class E(C,D):
    pass


'''
E->D->C->B->A
L(E(C,D)) = E + merge(L(C) ,L(D) ,(CD))
          = E + merge(DC,CB,BA)
          = E + D + merge(CB,BA,A)
          = E + D + C + merge(B,BA,A)
          = E + D + C + B + merge(A,A)
          = E -> B -> C ->D ->A
'''
print(inspect.getmro(E))

