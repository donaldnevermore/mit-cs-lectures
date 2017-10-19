# 背包问题
# w重量，v价值，i索引，aW总重量
def maxVal(w, v, i, aW):
    global numCalls
    numCalls += 1
    if i == 0:
        if w[i] <= aW:
            return v[i]
        else:
            return 0
    without_i = maxVal(w, v, i - 1, aW)
    if w[i] > aW:
        return without_i
    else:
        with_i = v[i] + maxVal(w, v, i - 1, aW - w[i])
    return max(with_i, without_i)


def fastMaxValue(weight, value, index, allWeight, memory):
    global count
    count += 1
    try:
        return memory[(index,allWeight)]
    except KeyError:
        if index == 0:
            if weight[index] <= allWeight:
                memory[(index,allWeight)]=value[index]
                return value[index]
            else:
                memory[(index,allWeight)]=0
                return 0
        without_index = fastMaxValue(weight, value, index-1, allWeight,memory)
        if weight[index] > allWeight:
            memory[(index,allWeight)]=without_index
            return without_index
        else:
            with_index = value[index] + fastMaxValue(weight, value, index-1, allWeight - weight[index],memory)
        result=max(with_index,without_index)
        memory[(index,allWeight)]=result
        return result



numCalls=0
count = 0
w = [5, 3, 2,5,7,8,6,7,10,1,3,4,5,6,7,8,8,1,1,5,7,6,2,1,8,4,2,8]
v = [9, 7, 8,3,4,5,6,10,9,8,7,8,6,5,4,3,5,7,8,2,0,3,2,0,7,5,6,9]
ww=[5,3,2]
vv=[9,7,8]
i = len(ww) - 1
aW = 5
memo={}
print(fastMaxValue(ww, vv, i, aW,memo),memo,count)
print(maxVal(w,v,i,aW),numCalls)

