# 汉诺塔递归算法
count = 0


def towers(size, fromStack, toStack, spareStack):
    if size == 1:
        print('Move disk from', fromStack, 'to', toStack)
        global count
        count += 1
    else:
        towers(size - 1, fromStack, spareStack, toStack)
        towers(1, fromStack, toStack, spareStack)
        towers(size - 1, spareStack, toStack, fromStack)


towers(2, 'f', 't', 's')
print('number of steps:', count)
