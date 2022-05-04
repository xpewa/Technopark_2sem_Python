import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_one_set(self):
        cache = LRUCache(3)
        cache.set("k1", "val1")
        self.assertEqual("val1", cache.get("k1"))

        self.assertEqual("k1", cache.head.key)
        self.assertEqual("k1", cache.tail.key)

    def test_set_node_in_cache(self):
        cache = LRUCache(3)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k1", "val10")
        self.assertEqual("val10", cache.get("k1"))
        self.assertEqual("val2", cache.get("k2"))

        self.assertEqual("k2", cache.head.key)

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
        self.assertEqual("val5", cache.get("k5"))
        self.assertEqual("val4", cache.get("k4"))
        self.assertEqual("val3", cache.get("k3"))

        self.assertEqual(3, cache.current_count)
        self.assertEqual("k3", cache.head.key)
        self.assertEqual("k5", cache.tail.key)

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
        self.assertEqual("val1", cache.get("k1"))

        self.assertEqual("k1", cache.head.key)
        self.assertEqual("k1", cache.tail.key)
        self.assertEqual(1, cache.current_count)

        cache.set("k2", "val2")
        self.assertEqual("val2", cache.get("k2"))
        self.assertEqual(None, cache.get("k1"))

        self.assertEqual("k2", cache.head.key)
        self.assertEqual("k2", cache.tail.key)
        self.assertEqual(1, cache.current_count)
        self.assertEqual(None, cache.head.next)
        self.assertEqual(None, cache.tail.prev)

    def test_task(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertEqual(None, cache.get("k3"))
        self.assertEqual("val2", cache.get("k2"))
        self.assertEqual("val1", cache.get("k1"))
        cache.set("k3", "val3")
        self.assertEqual("val3", cache.get("k3"))
        self.assertEqual(None, cache.get("k2"))
        self.assertEqual("val1", cache.get("k1"))

    def test_replace_all_nodes(self):
        cache = LRUCache(3)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        cache.set("k4", "val4")
        cache.set("k5", "val5")
        cache.set("k6", "val6")
        self.assertEqual("val5", cache.get("k5"))
        self.assertEqual("val4", cache.get("k4"))
        self.assertEqual("val6", cache.get("k6"))
        self.assertEqual(None, cache.get("k1"))
        self.assertEqual(None, cache.get("k2"))
        self.assertEqual(None, cache.get("k3"))

    def test_change_node_and_add_new(self):
        cache = LRUCache(3)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        self.assertEqual("val1", cache.get("k1"))
        cache.set("k4", "val4")
        self.assertEqual("val1", cache.get("k1"))
        self.assertEqual(None, cache.get("k2"))


if __name__ == "__main__":
    unittest.main()
