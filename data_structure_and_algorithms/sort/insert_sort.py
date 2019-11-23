def insertion_sort(arr):
    """
    插入排序 
    稳定性：稳定
    复杂度：
    平均 O(n^2)
    最坏 O(n^2)
    最好 O(n)

    从第1个元素开始，与左边n-1个元素进行比较，依次从右向左移动，
    插入到左侧已排序的元素，直到最左侧；
    然后从第2个元素开始，
    重复直到最右侧的元素。
    """
    n = len(arr)

    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


a = [5, 1, 4, 3, 2, 6]
insertion_sort(a)
print(a)
