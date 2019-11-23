def select_sort(arr):
    """
    选择排序
    稳定性：不稳定
    复杂度：
    平均 O(n^2)
    最坏 O(n^2)
    最好 O(n^2)

    1. 找到数组中最小的那个元素中，
    2. 将它和数组的第一个元素交换位置，
    3. 在剩下的元素中找到最小的元素，将它和数组的第二个元素交换位置，
    4. 如此往复，知道将整个数组排序。
    """
    # 索引从 0 到 n-2
    for i in range(len(arr) - 1):
        # 最小元素的索引
        min = i
        # min 与从 i+1 到 n-1 的元素比较
        j = i + 1
        while j < len(arr):
            if arr[min] > arr[j]:
                # 找到最小的元素
                min = j
            j += 1
        # 交换位置
        arr[i], arr[min] = arr[min], arr[i]


a = [5, 1, 4, 3, 2, 6]
select_sort(a)
print(a)
