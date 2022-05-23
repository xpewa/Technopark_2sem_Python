import weakref
import cProfile
import pstats
import io
from memory_profiler import profile

from lru_cache import LRUCache


class BookOrdinal:
    def __init__(self, tittle, author, count):
        self.tittle = tittle
        self.author = author
        self.count_in_library = count


class BookSlot:
    __slots__ = ("tittle", "author", "count_in_library")

    def __init__(self, tittle, author, count):
        self.tittle = tittle
        self.author = author
        self.count_in_library = count


@profile
def mem_stat():
    cache1 = LRUCache(1_000)
    for i in range(100_000):
        cache1.set(i, BookOrdinal("Tittle", "Author", 100))
    cache2 = LRUCache(1_000)
    for i in range(100_000):
        cache2.set(i, BookSlot("Tittle", "Author", 100))
    cache3 = LRUCache(1_000)
    node = BookOrdinal("Tittle", "Author", 100)
    for i in range(100_000):
        cache3.set(i, weakref.ref(node))


if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()

    mem_stat()

    pr.disable()

    out = io.StringIO()
    ps = pstats.Stats(pr, stream=out)
    ps.print_stats()

    print(out.getvalue())
