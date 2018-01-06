def bubbleSort(L):
    '''
    冒泡排序
    最佳情况：T(n) = O(n) 
    最差情况：T(n) = O(n*n) 
    平均情况：T(n) = O(n*n)
    '''
    swap = True
    while swap:
        print(L)
        swap = False
        for j in range(len(L) - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                swap = True


test = [1, 5, 4, 3, 2, 6, 67, 32, 90, 19, 66, 25, 3]
bubbleSort(test)
