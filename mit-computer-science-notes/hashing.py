# 哈希映射
def charSetCreate():
    charSet = []
    for i in range(0, 255):
        charSet.append(None)
    return charSet


def insert(charSet, e):
    charSet[hashChar(e)] = 1


def member(charSet, e):
    return charSet[e] == 1


def hashChar(c):
    return ord(c)



