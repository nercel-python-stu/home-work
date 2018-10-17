def insert(nums):
    '''
    param nums=list[int]
    两层循环，时间复杂度为O（n）
    '''
    #i表示每次插入时所操作数字的index
    i = 1
    while i < len(nums):
        j = i
        #若该数字比前面数字小那么就进行位置交换，直到第一个数字为止
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
        i += 1
    return nums

def test_insert():
    nums = [6, 5, 4, 3, 2, 1]
    insert(nums)
    print(nums)


def quick(nums, low, high):
    '''
    分治法，选取pivot，进行分类，让pivot之前的数字小于它，之后的大于它
    然后对pivot前后的两个子数组进行相同的操作，直到剩下一个数字为止
    每次都将问题的规模减半，时间复杂度为O（nlogn）
    '''
    if low < high:
        pivot = partition(nums, low, high)
        quick(nums, low, pivot)
        quick(nums, pivot+1, high)


def partition(nums, low, high):
    #这里选取第一个数作为pivot
    pivot = nums[low]
    while low < high:
        #high指针从尾部开始，若是比pivot大，那么往前移动
        #若是比pivot小，那么与low指针所指数字交换
        while nums[high] > pivot and low < high:
            high -= 1
        nums[low] = nums[high]
        #low指针同理
        while nums[low] < pivot and low < high:
            low += 1
        nums[high] = nums[low]
    nums[low] = pivot
    return low


def test_quick():
    nums = [6, 5, 4, 3, 2, 1]
    quick(nums, 0, len(nums)-1)
    print(nums)


def prime_number(n, result):
    '''
    外层是从2到n的一次遍历
    内层判断i是否是素数：因为一个数的最大因数不会大于它本身的平方根，
    因此将除数的范围限定在2到根号i之间
    因此时间复杂度为O(n*根号n)=O(n^1.5)
    '''
    for i in range(2, n):
        #用true和false来判断一个数是否要加进result数组里面
        flag = True
        for j in range(2, int(i ** 0.5)+1):
            if i % j == 0:
                flag = False
                break
        if flag:
            result.append(i)
    return result


def test_prime():
    result = []
    prime_number(1000000, result)
    print(result)


#test_insert()
#test_quick()
#test_prime()