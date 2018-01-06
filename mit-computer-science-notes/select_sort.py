def selectSort(L):
    '''
    最佳情况：T(n) = O(n*n) 
    最差情况：T(n) = O(n*n) 
    平均情况：T(n) = O(n*n)
    '''
    print('original:', L)
    for i in range(len(L) - 1):
        minIndex = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndex = j
                minVal = L[j]
            j = j + 1
        L[i], L[minIndex] = L[minIndex], L[i]
    print('sorted:', L)


test = [1, 5, 4, 3, 2, 6]
selectSort(test)
