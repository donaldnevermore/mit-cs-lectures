import random


def conflict(state, next_x):
    """Check if the queen would be eaten."""
    next_y = len(state)
    for i in range(next_y):
        if abs(state[i] - next_x) in (0, next_y - i):
            return True
    return False


def queens(num=8, state=()):
    """Brute force the last queen."""
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def pretty_print(solution):
    def line(pos, length=len(solution)):
        return ". " * pos + "X " + ". " * (length - pos - 1)

    for pos in solution:
        print(line(pos))


if __name__ == "__main__":
    answer = random.choice(list(queens(10)))
    pretty_print(answer)
