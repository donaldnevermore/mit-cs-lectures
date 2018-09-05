# left是原列表的左半部分
# 合并两个列表


def merge(left, right):
    """
    归并排序
    复杂度 O(n*log(n))
    """

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


def merge_sort(arr):
    print(arr)
    if len(arr) <= 2:
        # 当列表只有两个元素时排好序，减少步骤
        if len(arr) == 2 and arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr[:]
    else:
        middle = len(arr) // 2  # 分解列表，只能为整数
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        together = merge(left, right)
        print('merged', together)
        return together


left = [3, 12, 17, 24]
right = [1, 2, 4, 15]
test = [1, 5, 8, 3, 56, 24, 35, 99, 88, 22]
merge_sort(test)
