# 优化过的平方根算法
def square_root_nr(x, epsilon):
    assert x >= 0, 'x must be greater than 0' + str(x)
    assert epsilon > 0, 'x must be greater than 0' + str(x)
    guess = x / 2
    count = 1
    diff = guess**2 - x
    while abs(diff) > epsilon and count <= 100:
        guess = guess - diff / (2 * guess)
        diff = guess**2 - x
        count += 1
    print(count, guess)
    return guess


square_root_nr(123456789, 0.0001)
square_root_nr(123456789, 0.1)
