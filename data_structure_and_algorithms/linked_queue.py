from typing import TypeVar, Generic, Optional, Union, NoReturn
from dataclasses import dataclass

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    item: T
    next: Optional["Node"]


class Queue(Generic[T]):
    first: Optional[Node]
    last: Optional[Node]
    n: int

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.n = 0

    def is_empty(self) -> bool:
        return self.first is None

    def enqueue(self, item: T) -> None:
        old_last = self.last
        self.last = Node(item, None)
        if self.is_empty():
            self.first = self.last
        else:
            assert old_last is not None
            old_last.next = self.last

        self.n += 1

    def dequeue(self) -> Union[T, NoReturn]:
        if self.is_empty():
            raise Exception("队列为空，无法出列")

        assert self.first is not None
        item: T = self.first.item
        self.first = self.first.next
        # 队列从非空变为空
        if self.is_empty():
            self.last = None

        self.n -= 1
        return item

    def __len__(self) -> int:
        return self.n
