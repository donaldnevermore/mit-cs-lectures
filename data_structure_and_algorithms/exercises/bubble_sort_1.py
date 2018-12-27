def bubble_sort(arr):
    swap = True

    while swap:
        swap = False

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True


a = [5, 1, 4, 3, 2, 6]
bubble_sort(a)
print(a)
