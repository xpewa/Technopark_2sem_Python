from dataclasses import dataclass
from logging import StreamHandler, FileHandler
import logging
import sys


def new_loger(file="cache.log", encoding="utf-8"):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formater_file = logging.Formatter(fmt="%(asctime)s - "
                                      "%(module)s - %(levelname)s :"
                                      "- %(message)s")
    formater_stdout = logging.Formatter(fmt="%(levelname)s : - %(message)s")

    file_handler = FileHandler(file, encoding=encoding)
    file_handler.setFormatter(formater_file)
    logger.addHandler(file_handler)

    if "-s" in sys.argv:
        stream_handler = StreamHandler(stream=sys.stdout)
        stream_handler.setFormatter(formater_stdout)
        logger.addHandler(stream_handler)

    return logger


log = new_loger()


class LRUCache:

    @dataclass
    class LRUNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None
            log.debug("Create LRUNode with key = %s", key)

    def __init__(self, limit=42):
        self.limit = limit
        self.current_count = 0
        self.dict = {}
        self.head = None
        self.tail = None
        log.debug("Create LRUCache")

    def _move_to_head(self, node):
        self._delete_node(node)
        self._set_node(node)

    def _set_node(self, node):
        if node:
            if self.head:
                self.head.prev = node
                node.next = self.head
            else:
                self.tail = node
            self.head = node
            self.current_count += 1
            log.debug("Set head with key = %s", node.key)

    def _delete_node(self, node):
        if node:
            next_node = node.next
            prev_node = node.prev
            if next_node:
                next_node.prev = node.prev
                if next_node.prev is None:
                    self.head = next_node
            if prev_node:
                prev_node.next = node.next
                if prev_node.next is None:
                    self.tail = prev_node
            if not next_node and not prev_node:
                self.head = None
                self.tail = None
            self.current_count -= 1
            log.debug("Delete node with key = %s", node.key)
        log.warning("Try deleted None")

    def get(self, key):
        node = self.dict.get(key)
        if node:
            self._move_to_head(node)
            log.info("Get node with key = %s", key)
            return self.head.value

        log.warning("Get not exist node")
        return None

    def set(self, key, value):
        if key in self.dict:
            self.dict[key].value = value
            self._move_to_head(self.dict.get(key))
            log.info("Changing the value in node with key = %s", key)
            return

        if self.current_count == self.limit:
            self.dict.pop(self.tail.key)
            self._delete_node(self.tail)

        node = LRUCache.LRUNode(key, value)
        self._set_node(node)
        self.dict[key] = node
        log.info("Set node with key = %s", key)


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    print(cache.get("k3"))  # None
    print(cache.get("k2"))  # "val2"
    print(cache.get("k1"))  # "val1"

    cache.set("k3", "val3")

    print(cache.get("k3"))  # "val3"
    print(cache.get("k2"))  # None
    print(cache.get("k1"))  # "val1"
    print(cache.current_count)
