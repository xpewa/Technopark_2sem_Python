import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_set(self):
        cache = LRUCache(3)
        cache.set("k1", "val1")
        self.assertEqual("k1", cache.head.key)
        self.assertEqual("k1", cache.tail.key)

    def test_get(self):
        cache = LRUCache(3)
        cache.set("k1", "val1")
        self.assertEqual("val1", cache.get("k1"))
        self.assertEqual(1, cache.current_count)

    def test_set_node_in_cache(self):
        cache = LRUCache(3)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k1", "val10")
        self.assertEqual("k1", cache.head.key)
        self.assertEqual("val10", cache.get("k1"))

    def test_count_after_set_one_node(self):
        cache = LRUCache(3)
        cache.set("k1", "val1")
        self.assertEqual(1, cache.current_count)

    def test_count_after_set_nodes(self):
        cache = LRUCache(3)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        cache.set("k4", "val4")
        cache.set("k5", "val5")
        self.assertEqual(3, cache.current_count)
        self.assertEqual("k5", cache.head.key)
        self.assertEqual("k3", cache.tail.key)

    def test_get_node_not_in_cache(self):
        cache = LRUCache(3)
        self.assertEqual(None, cache.get("k1"))

    def test_get_node_was_in_cache(self):
        cache = LRUCache(3)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        cache.set("k4", "val4")
        self.assertEqual(None, cache.get("k1"))

    def test_get_node_in_cache(self):
        cache = LRUCache(3)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        cache.set("k4", "val4")
        self.assertEqual("val3", cache.get("k3"))
        self.assertEqual("k3", cache.head.key)

    def test_limit_1(self):
        cache = LRUCache(1)
        cache.set("k1", "val1")
        self.assertEqual("k1", cache.head.key)
        self.assertEqual("k1", cache.tail.key)
        self.assertEqual(1, cache.current_count)
        cache.set("k2", "val2")
        self.assertEqual("k2", cache.head.key)
        self.assertEqual("k2", cache.tail.key)
        self.assertEqual(1, cache.current_count)
        self.assertEqual(None, cache.head.next)
        self.assertEqual(None, cache.tail.prev)


if __name__ == "__main__":
    unittest.main()
