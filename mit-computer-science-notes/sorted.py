#coding:utf-8
# 选择排序
def selSort(L):
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


test1 = [1, 5, 4, 3, 2, 6]

# selSort(test1)

# 冒泡排序
def bubbleSort(L):
    swap = True
    while swap:
        print(L)
        swap = False
        for j in range(len(L) - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                swap = True


bubbleSort(test1)
