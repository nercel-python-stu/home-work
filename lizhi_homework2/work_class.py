'''
使用元类实现单例模式
调用__call__的时候只创建一个实例
'''
class Singleton(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance
 
 
class Foo(metaclass=Singleton):
    pass
 
 
foo1 = Foo()
foo2 = Foo()
#验证foo1和foo2是同一个实例
#print(foo1 is foo2)

'''
将作业转化为类实现
'''
class sort_num:
    #定义基本属性
    nums = []
    def __init__(self,n):
        self.nums = n
    def insert(self):
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1
            i += 1
        return nums

nums = [6, 5, 4, 3, 2, 1]
# 实例化类
p = sort_num(nums)
p.insert()
print(nums)