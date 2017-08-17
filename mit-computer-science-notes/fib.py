def fib(n):
    global numCalls
    numCalls += 1
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fastFib(n):
    global numCalls
    global memo
    numCalls += 1
    print("fib1 called with", n)
    if n not in memo:
        memo[n] = fastFib(n - 1) + fastFib(n - 2)
    return memo[n]


numCalls = 0
n = 30
memo = {0: 1, 1: 1}
# print('fib of', n, '=', fib(n), 'numCalls=', numCalls)
# print(fastFib(30),"numCalls=",numCalls)
