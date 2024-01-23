def fib(n):
    fibList = [1,1]
    if n==1 or n==2:
        return 1
    for i in range(2, n):
        fibList.append(fibList[i-1] + fibList[i-2])
    return fibList[n-1]

def solution(n):
    return fib(n) % 1234567