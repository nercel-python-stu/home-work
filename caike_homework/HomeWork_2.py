# -*- coding: utf-8 -*-
import re
#验证手机号是否正确
#判断手机号的前三位,可以为13[0-9]、145、147、15[0-9]、166、173、176、177、18[0-9]
#用该正则表达式去匹配用户的输入来判断是否合法。
#创建匹配11位手机号的正则表达式
#match()方法判断是否匹配。

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton,cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class Test_Phone(Singleton):
	def y_phone(self,phone):
		p= re.match(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$',phone)
		if p:
			print(phone,"：这是正确的手机号码！")
		else:
			print(phone,"：这不是正确的手机号码！")

if __name__ == '__main__':
    #输入验证手机号
    print('验证手机号')
    Test_A = Test_Phone()	
    Test_A.y_phone('123456789')
    Test_A.y_phone('14411111111')
    Test_A.y_phone('18720994197')
    phone=input("再输入手机号进行验证：")
    Test_A.y_phone(phone)
    print('\n')
