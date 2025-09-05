import math

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
    p = int(input("Something:"))
    n = 2
    count = 0
    if p <=1:
        print("Nothing")
    else:
        while count < p:
            if ex5(n):
                print(n, end=",")
                count += 1
            n +=1


def divisors(n):
    ds =[]
    for i in range(1,n):
        if n % i == 0:
            ds.append(i)
    return ds
def is_perfect(n):
    return sum(divisors(n)) == n
for num in range(1,1000):
    if is_perfect(num):
        print(f"{num} is perfect. Divisors: {divisors(num)}")


def is_pangram(s):
    pr = s.lower()
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c not in pr:
            return False
    return True
if __name__ == '__main__':
    print(is_pangram("Hello"))