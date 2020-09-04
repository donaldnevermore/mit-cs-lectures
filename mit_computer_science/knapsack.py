def max_value(weights, values, index, weight_available):
    """背包问题

    :param weights: 重量
    :param values: 价值
    :param index: 索引，默认从最后一个开始
    :param weight_available: 可用重量
    :return: 最大价值
    """
    global num_calls
    num_calls += 1

    if index == 0:
        if weights[index] <= weight_available:
            # Packed if not full.
            return values[index]
        else:
            return 0

    # Not packed.
    without_index = max_value(weights, values, index - 1, weight_available)

    if weights[index] > weight_available:
        # The knapsack is full.
        return without_index
    else:
        with_index = values[index] + max_value(weights, values, index - 1, weight_available - weights[index])
        return max(with_index, without_index)


def fast_max_value(weights, values, index, weight_available, memory):
    global count
    count += 1

    if (index, weight_available) in memory:
        return memory[(index, weight_available)]

    if index == 0:
        if weights[index] <= weight_available:
            memory[(index, weight_available)] = values[index]
            return values[index]
        else:
            memory[(index, weight_available)] = 0
            return 0

    without_index = fast_max_value(weights, values, index - 1, weight_available, memory)

    if weights[index] > weight_available:
        memory[(index, weight_available)] = without_index
        return without_index
    else:
        with_index = values[index] + fast_max_value(weights, values, index - 1, weight_available - weights[index],
                                                    memory)
        result = max(with_index, without_index)
        memory[(index, weight_available)] = result
        return result


num_calls = 0
count = 0
weight_available = 5
memo = {}

weights = [5, 3, 2, 5, 7, 8, 6, 7, 10, 1, 3, 4, 5, 6, 7, 8, 8, 1, 1, 5, 7, 6, 2, 1, 8, 4, 2, 8]
values = [9, 7, 8, 3, 4, 5, 6, 10, 9, 8, 7, 8, 6, 5, 4, 3, 5, 7, 8, 2, 0, 3, 2, 0, 7, 5, 6, 9]
print(fast_max_value(weights, values, len(weights) - 1, weight_available, memo))
print(memo)
print(count)

weights2 = [5, 3, 2]
values2 = [9, 7, 8]
print(max_value(weights2, values2, len(weights2) - 1, weight_available), num_calls)
