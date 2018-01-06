# 二分查找法求平方根
def squareRootBi(x, epsilon):
    '''x>=0,epsilon>=0'''
    assert x >= 0, "x must be greater than zero" + str(x)
    assert epsilon > 0, "epsilon must be greater than zero" + str(epsilon)
    low = 0
    high = max(x, 1)
    guess = (low + high) / 2
    count = 1
    while abs(guess**2 - x) > epsilon and count <= 100:
        # print("low:",low,"high:",high,"guess",guess)
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
        count += 1
    assert count <= 100, "iterate count"
    print(count, guess)
    return guess


squareRootBi(123456789, 0.0001)
