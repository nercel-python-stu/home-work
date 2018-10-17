import math

def prime(n):
    if n <= 1:
        return False
#素数个数;for(i=2;i<(n=sqrt(n));i++)
#i在2到sqrt(n)之间任取一个数,如果n能被整除则i不是素数，否则i就是素数
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def prime_num(n):
    primes = [2]
    for i in range(3, n + 1, 2):
        if prime(i):
            primes.append(i)
    return len(primes)

print (prime_num(1000000))
