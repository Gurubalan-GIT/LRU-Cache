from abc import ABC

from custom_collections.linked_list.ll import BaseNode as Node, BaseLinkedList


class LinkedList(BaseLinkedList, ABC):

    def prepend(self, value) -> None:
        node = Node(value)
        node.next = self.head
        self.head = node

        if not self.tail:
            self.tail = node

    def append(self, value) -> None:
        node = Node(value)
        if not self.head:
            self.head = node

        if self.tail:
            self.tail.next = node

        self.tail = node

    def find(self, value) -> None or Node:
        if not self.head:
            return None
        curr: Node = self.head
        while curr:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    def insert_after(self, prev_value, value) -> None:
        prev_node: Node = self.find(prev_value)
        if prev_node:
            new_node = Node(value)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def delete_head(self) -> None or Node:
        if self.head:
            deleted_head = self.head
            self.head = self.head.next
            return deleted_head
        else:
            self.head = None
            self.tail = None
        return None

    def delete_all_occurrences(self, value) -> None:
        if not self.head:
            return None

        if self.head.value == value:
            self.delete_head()

        curr: Node = self.head

        while curr.next:
            if curr.next.value == value:
                if curr.next.value == self.head.value:
                    self.head = self.head.next.next
                curr.next = curr.next.next
            else:
                curr = curr.next

        if self.tail == value:
            self.tail = curr
