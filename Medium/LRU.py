# solution1: we need fast lookups -> Hash Table and fast removals ->     
# doubly liked list to implement it we need dummy head and dummy tail
#since we only add to the front and remove from end then timecomplexity
#is in constant time
#TimeComplexity: O(1)
#SpaceComplexity: O(n)
# solution2: Use Ordered Dict
class LRUCache:

    class Node:
        def __init__(self, key, data, prev, next):
            self.key = key  # keep track of key so we can delete from table
            self.data = data
            self.prev = prev
            self.next = next
        
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}  # key: node
        self.head = None
        self.tail = None
        self.size = 0
        
    def _empty(self):
        return self.size == 0
    
    def _popLast(self):
        node = self.tail
        self.tail = self.tail.prev
        self.size -= 1
        if self._empty():
            self.head = None
        else:
            self.tail.next = None
        return node
    
    def _popFirst(self):
        node = self.head
        self.head = self.head.next
        self.size -= 1
        if self._empty():
            self.tail = None
        else:
            self.head.prev = None
        return node
    
    def _prepend(self, key, value):
        if self._empty():
            node = self.Node(key, value, None, None)
            self.head = node
            self.tail = node
        else:
            node = self.Node(key, value, None, self.head)
            self.head.prev = node
            self.head = node
        self.table[key] = self.head
        self.size += 1

    def _remove(self, node):
        if node.prev == None:
            return self._popFirst()
        if node.next == None:
            return self._popLast()    
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node
        
    def get(self, key: int) -> int:
        if key in self.table:
            node = self._remove(self.table[key])
            self._prepend(key, node.data)
            return node.data
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self._remove(self.table[key])
            self._prepend(key, value)      
        else:
            if self.size < self.capacity:
                self._prepend(key, value)
            else:
                node = self._popLast()
                del self.table[node.key]
                self._prepend(key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

### ** ordered Dict**
```python
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
