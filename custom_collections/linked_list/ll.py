import abc
from typing import Union


class BaseNode:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class BaseLinkedList:

    def __init__(self) -> None:
        self.head: Union[BaseNode, None] = None
        self.tail: Union[BaseNode, None] = None

    @abc.abstractmethod
    def to_list(self) -> list:
        node_list = list()
        curr: Union[BaseNode] = self.head
        while curr:
            node_list.append(curr.value)
            curr = curr.next

        return node_list
