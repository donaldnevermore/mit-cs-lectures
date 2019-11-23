def bubble_sort(arr):
    """
    冒泡排序
    稳定性：稳定
    复杂度：
    平均 O(n^2)
    最坏 O(n^2)
    最好 O(n)

    如果需要交换
    从第0个元素开始，与右边的一个元素比较，
    再从第1个开始比较，与右边的一个元素比较，最大的元素会冒泡到最右侧
    重复直到不再需要交换
    """
    swap = True
    while swap:
        print(arr)
        swap = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True


a = [5, 1, 4, 3, 2, 6]
bubble_sort(a)
