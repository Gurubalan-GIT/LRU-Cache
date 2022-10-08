from custom_collections.linked_list.dll import *


class LRUNode(Node):
    def __init__(self, key: int, value):
        super().__init__(value)
        self.key = key

    def __repr__(self):
        return f"Key: {self.key}, Value: {self.value}"

    def __str__(self):
        return f"Key: {self.key}, Value: {self.value}"


class LRUCache(DoublyLinkedList, ABC):

    def __init__(self, capacity: int):
        super().__init__()
        self.lru_map = {}
        self.capacity = capacity

    def delete_from_cache(self, node: LRUNode):
        self.unlink(node)
        del self.lru_map[node.value.key]
        del node

    def evict_lru_from_cache(self):
        if not self.tail:
            return None

        lru_node: LRUNode = self.tail
        self.delete_from_cache(lru_node)

    def get(self, key: int) -> int:
        if key not in self.lru_map:
            return -1

        node = self.lru_map[key]

        if self.head != node:
            self.unlink(node)
            self.prepend(node)

        return node.value

    def put(self, key: int, value):
        new_node = LRUNode(key, value)
        if key in self.lru_map:
            self.delete_from_cache(self.lru_map[key])

        if len(self.lru_map) >= self.capacity:
            self.evict_lru_from_cache()

        self.prepend(new_node)
        self.lru_map[key] = new_node
