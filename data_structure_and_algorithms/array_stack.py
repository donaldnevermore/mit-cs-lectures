from typing import List, TypeVar, Generic

T = TypeVar("T")


class Stack(Generic[T]):
    a: List[T]

    def __init__(self) -> None:
        self.a = []

    def is_empty(self) -> bool:
        return len(self.a) == 0

    def __len__(self) -> int:
        return len(self.a)

    def push(self, item: T) -> None:
        self.a += [item]

    def pop(self) -> T:
        return self.a.pop()
