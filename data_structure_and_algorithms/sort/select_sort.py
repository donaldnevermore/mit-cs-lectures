def select_sort(arr):
    """
    选择排序 不稳定

    复杂度
    所有情况 O(n^2)

    每次从待排序的元素中选出最小的，放在最左侧，直到所有待排序的元素排完。

    从第0个元素开始，与右侧n-1个元素比较，选择到最小值，放到第1个；
    然后第1个元素，以此类推。
    """
    print('original:', arr)
    for i in range(len(arr) - 1):
        min_index = i
        min_val = arr[i]
        j = i + 1
        while j < len(arr):
            if min_val > arr[j]:
                min_index = j
                min_val = arr[j]
            j = j + 1
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print('sorted:', arr)


a = [5, 1, 4, 3, 2, 6]
select_sort(a)
