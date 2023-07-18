from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Since the item is get, move to recently used
        self.cache.move_to_end(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        # Since the item is already in the cache, remove to simulate update
        # This should be done first before removing the LRU
        if key in self.cache:
            self.cache.pop(key)

        # Remove the LRU
        if len(self.cache) == self.capacity:
            self.cache.popitem(False)
        
        # Update or create the item
        self.cache[key] = value
       


# lRUCache = LRUCache(2)
# print(lRUCache.put(1, 1))   # cache is {1=1}
# print(lRUCache.put(2, 2))   # cache is {1=1, 2=2}
# print(lRUCache.get(1))      # return 1
# print(lRUCache.put(3, 3))   # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(lRUCache.get(2))      # returns -1 (not found)
# print(lRUCache.put(4, 4))   # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# print(lRUCache.get(1))      # return -1 (not found)
# print(lRUCache.get(3))      # return 3
# print(lRUCache.get(4))      # return 4

# lRUCache = LRUCache(2)
# print(lRUCache.put(2, 1))
# print(lRUCache.put(2, 2))
# print(lRUCache.get(2))
# print(lRUCache.put(1, 1))
# print(lRUCache.put(4, 2))
# print(lRUCache.get(2))

lRUCache = LRUCache(2)
print(lRUCache.get(2))
print(lRUCache.put(2, 6))
print(lRUCache.get(1))
print(lRUCache.put(1, 5))
print(lRUCache.put(1, 2))
print(lRUCache.get(1))
print(lRUCache.get(2))