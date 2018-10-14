class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        """ 弹出第1个 """
        item = self.head.item
        self.head = self.head.next
        return item


class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next
