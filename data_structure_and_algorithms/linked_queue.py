class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def is_empty(self):
        return self.first is None

    def enqueue(self, item):
        old_last = self.last
        self.last = Node(item, None)

        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last

        self.length += 1

    def dequeue(self):
        item = self.first.item
        self.first = self.first.next

        if self.is_empty():
            self.last = None

        self.length -= 1

        return item

    def __len__(self):
        return self.length


class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next
