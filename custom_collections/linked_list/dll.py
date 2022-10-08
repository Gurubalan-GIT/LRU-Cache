from abc import ABC
from typing import Union

from custom_collections.linked_list.ll import BaseNode, BaseLinkedList


class Node(BaseNode):

    def __init__(self, value) -> None:
        super().__init__(value)
        self.prev = None


class DoublyLinkedList(BaseLinkedList, ABC):

    def prepend(self, value) -> None:
        new_node = Node(value)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

        if not self.tail:
            self.tail = new_node

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node

    def find(self, value) -> None or Node:
        if not self.head:
            return None
        curr: Node = self.head
        while curr:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    def delete_head(self) -> None or Node:
        if self.head:
            deleted_head = self.head
            self.head = self.head.next
            self.head.prev = None
            return deleted_head
        else:
            self.head = None
            self.tail = None
        return None

    def delete_all_occurrences(self, value) -> None:
        if not self.head:
            return None

        curr: Node = self.head

        while curr:
            if curr.value == value:
                if self.head.value == curr.value:
                    self.delete_head()
                if curr.prev:
                    curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
            curr = curr.next

        if self.tail.value == value:
            self.tail = curr.prev

    def unlink(self, node: Union[Node, None]):
        if not node:
            return None

        prev_node: Node = node.prev
        next_node: Node = node.next

        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

        if self.head == node:
            self.head = next_node

        if self.tail == node:
            self.tail = prev_node

        node.prev = None
        node.next = None
