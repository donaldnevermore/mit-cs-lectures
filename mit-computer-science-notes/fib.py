# 斐波那契数列
def fib(n):
    global num_calls
    numCalls += 1
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fastFib(n: int):
    global num_calls
    global memo
    numCalls += 1
    print("fib1 called with", n)
    if n not in memo:
        memo[n] = fastFib(n - 1) + fastFib(n - 2)
    return memo[n]


num_calls = 0
n = 30
memo = {0: 1, 1: 1}

print(f'fib of {n} = {fib(n)}, numCalls = {num_calls}')
print(f'{fastFib(30)}, numCalls={num_calls}')
