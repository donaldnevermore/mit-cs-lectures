def exp1(a, b):
    answer = 1
    if a == 0:
        answer = 0
        return answer
    while b > 0:
        answer *= a
        b -= 1
    return answer


def exp2(a, b):
    if b == 1:
        return a
    else:
        return a * exp2(a, b - 1)


def exp3(a, b):
    if b == 1:
        return a
    if (b % 2) * 2 == b:
        return exp3(a * a, b / 2)
    else:
        return a * exp3(a, b - 1)


def multi(a, b):
    answer = 0
    for i in range(a):
        for j in range(b):
            answer += 1
    return answer


print(multi(2, 4))
