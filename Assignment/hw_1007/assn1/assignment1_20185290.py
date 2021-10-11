import time

#피보나치수열 - 반복 
def iterfib(n):
    a,b = 1,1
    if n==1 or n==2:
        return 1
    for i in range(1,n):
        a,b = b, a+b
    return a


#피보나치수열 - 재귀
def fib(n):
    if n==1 or n==2:
        return 1  
    return fib(n-1)+fib(n-2)

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfib(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fib(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
