def max_value(weight, value, index, available_weight):
    """背包问题

    :param weight: 重量
    :param value: 价值
    :param index: 索引，默认从最后一个开始
    :param available_weight: 可用重量
    :return: 最大价值
    """
    global num_calls
    num_calls += 1

    if index == 0:
        if weight[index] <= available_weight:
            # 还能装进背包，就放入
            return value[index]
        else:
            return 0

    # 不装进背包
    without_index = max_value(weight, value, index - 1, available_weight)

    if weight[index] > available_weight:
        # 装不下了
        return without_index
    else:
        with_index = value[index] + max_value(weight, value, index - 1, available_weight - weight[index])

    return max(with_index, without_index)


def fast_max_value(weight, value, index, available_weight, memory):
    global count
    count += 1

    try:
        return memory[(index, available_weight)]
    except KeyError:
        if index == 0:
            if weight[index] <= available_weight:
                memory[(index, available_weight)] = value[index]
                return value[index]
            else:
                memory[(index, available_weight)] = 0
                return 0

        without_index = fast_max_value(weight, value, index - 1, available_weight, memory)

        if weight[index] > available_weight:
            memory[(index, available_weight)] = without_index
            return without_index
        else:
            with_index = value[index] + fast_max_value(weight, value, index - 1, available_weight - weight[index],
                                                       memory)

        result = max(with_index, without_index)
        memory[(index, available_weight)] = result
        return result


num_calls = 0
count = 0
ww = [5, 3, 2, 5, 7, 8, 6, 7, 10, 1, 3, 4, 5, 6, 7, 8, 8, 1, 1, 5, 7, 6, 2, 1, 8, 4, 2, 8]
vv = [9, 7, 8, 3, 4, 5, 6, 10, 9, 8, 7, 8, 6, 5, 4, 3, 5, 7, 8, 2, 0, 3, 2, 0, 7, 5, 6, 9]
w = [5, 3, 2]
v = [9, 7, 8]
aw = 5
memo = {}
print(fast_max_value(ww, vv, len(ww) - 1, aw, memo))
print(memo)
print(count)
print(max_value(w, v, len(w) - 1, aw), num_calls)
