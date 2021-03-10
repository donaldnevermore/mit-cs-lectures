def char_set_create():
    char_set = []
    for i in range(0, 255):
        char_set.append(None)
    return char_set


def insert(char_set, e):
    char_set[hash_char(e)] = 1


def member(char_set, e):
    return char_set[e] == 1


def hash_char(c):
    return ord(c)
