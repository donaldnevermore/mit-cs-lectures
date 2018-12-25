"""
背包问题

weight重量，value价值，index索引，all_weight总重量
"""


def max_value(weight, value, index, all_weight):
    global num_calls
    num_calls += 1

    if index == 0:
        if weight[index] <= all_weight:
            return value[index]
        else:
            return 0

    without_index = max_value(weight, value, index - 1, all_weight)

    if weight[index] > all_weight:
        return without_index
    else:
        with_index = value[index] + max_value(weight, value, index - 1, all_weight - weight[index])

    return max(with_index, without_index)


def fast_max_value(weight, value, index, all_weight, memory):
    global count
    count += 1

    try:
        return memory[(index, all_weight)]
    except KeyError:
        if index == 0:
            if weight[index] <= all_weight:
                memory[(index, all_weight)] = value[index]
                return value[index]
            else:
                memory[(index, all_weight)] = 0
                return 0

        without_index = fast_max_value(weight, value, index - 1, all_weight, memory)

        if weight[index] > all_weight:
            memory[(index, all_weight)] = without_index
            return without_index
        else:
            with_index = value[index] + fast_max_value(weight, value, index - 1, all_weight - weight[index], memory)

        result = max(with_index, without_index)
        memory[(index, all_weight)] = result
        return result


num_calls = 0
count = 0
w = [5, 3, 2, 5, 7, 8, 6, 7, 10, 1, 3, 4, 5, 6, 7, 8, 8, 1, 1, 5, 7, 6, 2, 1, 8, 4, 2, 8]
v = [9, 7, 8, 3, 4, 5, 6, 10, 9, 8, 7, 8, 6, 5, 4, 3, 5, 7, 8, 2, 0, 3, 2, 0, 7, 5, 6, 9]
ww = [5, 3, 2]
vv = [9, 7, 8]
i = len(ww) - 1
aw = 5
memo = {}
print(fast_max_value(ww, vv, i, aw, memo), memo, count)
print(max_value(w, v, i, aw), num_calls)
