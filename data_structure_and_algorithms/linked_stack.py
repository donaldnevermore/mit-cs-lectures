from typing import TypeVar, Generic, Optional
from dataclasses import dataclass

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    item: T
    next: Optional["Node"]


class Stack(Generic[T]):
    head: Optional[Node]

    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, item: T) -> None:
        self.head = Node(item, self.head)

    def pop(self) -> T:
        """弹出第1个"""
        item: T = self.head.item
        self.head = self.head.next
        return item
