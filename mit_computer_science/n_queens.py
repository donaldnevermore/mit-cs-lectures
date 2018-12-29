import random


def conflict(state, next_x):
    """检查皇后能否被吃"""
    next_y = len(state)
    for i in range(next_y):
        if abs(state[i] - next_x) in (0, next_y - i):
            return True
    return False


def queens(num=8, state=()):
    """只剩一个皇后没放，穷举她的位置，递归太多影响性能"""
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def pretty_print(solution):
    """美化输出"""

    def line(pos, length=len(solution)):
        return '. ' * pos + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


def main():
    answer = random.choice(list(queens(10)))
    pretty_print(answer)


if __name__ == '__main__':
    main()
