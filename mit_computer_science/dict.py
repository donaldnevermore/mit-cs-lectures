# 结构化代码的示例

import math

# 字典的基本操作
dict1 = {1: "one", 2: "two", 3: "three"}
list1 = [[1, "one"], [2, "two"]]
del dict1[1]


# print(dict1)


def key_search(data, key):
    for elem in data:
        if elem[0] == key:
            return elem[1]
        else:
            return None


# print(key_search(list1, 1))

# 确保输入为浮点数
def get_float(requestMsg, errorMsg):
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
base = get_float("Enter a float", "Error: Base must be a floating point number")
height = get_float(
    "Enter a float", "Error: Height must be a floating point number")

#  毕达哥斯拉定理的第三条边的计算
hyp = math.sqrt(base * base + height * height)
print("base:" + str(base) + " height:" + str(height) + " hyp:" + str(hyp))
