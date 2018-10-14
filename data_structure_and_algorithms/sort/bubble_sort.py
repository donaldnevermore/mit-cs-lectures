def bubble_sort(arr):
    """
    冒泡排序 稳定

    复杂度
    最好 O(n)
    最坏 O(n^2)
    平均 O(n^2)

    如果需要交换
    从第0个元素开始，与右边的一个元素比较，
    再从第1个开始比较，与右边的一个元素比较，最大的元素会冒泡到最右侧
    重复直到不再需要交换
    """
    swap = True
    while swap:
        print(arr)
        swap = False
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True


a = [5, 1, 4, 3, 2, 6]
bubble_sort(a)
