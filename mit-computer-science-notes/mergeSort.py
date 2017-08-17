from sorted import selSort


# left是原列表的左半部分
# 合并两个列表
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    # 把比较大小后剩下的放进去
    while i < len(left):
        result.append(left[i])
        i = i + 1
    while j < len(right):
        result.append(right[j])
        j = j + 1
    return result


def mergeSort(L):
    print(L)
    if len(L) <= 2:
        # 当列表只有两个元素时排好序，减少步骤
        if len(L) == 2 and L[0] > L[1]:
            L[0], L[1] = L[1], L[0]
        return L[:]
    else:
        middle = int(len(L) / 2) # 分解列表，只能为整数
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        together = merge(left, right)
        print('merged', together)
        return together


left = [3, 12, 17, 24]
right = [1, 2, 4, 15]
test = [1, 5, 8, 3, 56, 24, 35, 99, 88, 22]
mergeSort(test)
# selSort(test)
