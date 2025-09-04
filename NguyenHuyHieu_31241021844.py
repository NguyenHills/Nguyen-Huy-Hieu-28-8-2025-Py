import math
import  random
def ex1(a,b,c):
    if a >= b and a >=c:
        return a
    if b >= a and b >= c:
        return b
    else:
        return c
def ex2(*args):
    return sum(args)
def ex3(s):
    return s[::-1]
def ex4(so):
    if so == 0:
        return 1
    else:
        return so*ex4(so-1)
def ex5(n:int)->bool:
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    else:
        return True
def ex61():
    n = int(input("Something:"))
    primes = []
    for i in range(2,n):
        if ex5(i):
            primes.append(i)
    print(primes)
def ex62():
    N = int(input("Something:"))
    n = 2
    count = 0
    if N <=1:
        print("Nothing")
    else:
        while count < N:
            if ex5(n):
                print(n, end=",")
                count += 1
            n +=1

if __name__ == '__main__':
    print(ex62())
