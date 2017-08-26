# 结构化代码的示例

import math

# 字典的基本操作
Dict1 = {1: 'one', 2: 'two', 3: 'three'}
L1 = [[1, 'one'], [2, 'two']]
del Dict1[1]
# print(Dict1)


def keySearch(L, k):
    for elem in L:
        if elem[0] == k:
            return elem[1]
        else:
            return None

# print(keySearch(L1, 1))

# 确保输入为浮点数
def getFloat(requestMsg, errorMsg):
    inputOK = False
    while not inputOK:
        try:
            val = float(input(requestMsg))
        except Exception:
            print(errorMsg)
        else:
            inputOK = True
        return val


# Get base and height
base = getFloat('Enter a float', 'Error: Base must be a floating point number')
height = getFloat(
    'Enter a float', 'Error: Height must be a floating point number')

#  毕达哥斯拉定理的第三条边的计算
hyp = math.sqrt(base * base + height * height)
print('base:' + str(base) + ' height:' + str(height) + ' hyp:' + str(hyp))
