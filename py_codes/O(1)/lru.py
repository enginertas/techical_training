class CacheNode():
    def __init__(self, key=None, val=None, prv=None, nxt=None):
        self._key = key
        self._value = val
        self._prev = prv
        self._next = nxt
        
    def __str__(self):
        ret_str = "(" + str(self._key) + "," + str(self._value) + ") "
        if self._next == None:
            return ret_str + "$"
        else:
            return ret_str + str(self._next)

class LRUCache(object):
    def __init__(self, capacity):
        self._capacity = capacity
        self._dict = {}
        self._qhead = CacheNode()
        self._qtail = self._qhead
        self._qsize = 0
        
    def _extractCacheNode(self, cache_node):
        if cache_node._prev:
            cache_node._prev._next = cache_node._next
        if cache_node._next:
            cache_node._next._prev = cache_node._prev

    def _insertCacheNode(self, key, cache_node):
        cache_node._prev = self._qtail
        self._qtail._next = cache_node
        self._qtail = self._qtail._next
        self._dict[key] = self._qtail
        cache_node._next = None
        
    def _updateCacheNodeOrder(self, key, cache_node):
        if cache_node != self._qtail:
            self._extractCacheNode(cache_node)
            self._insertCacheNode(key, cache_node)

    def get(self, key):
        if key not in self._dict:
            return -1
        else:
            cache_node = self._dict[key]
            self._updateCacheNodeOrder(key, cache_node)
            return cache_node._value

    def _putExisting(self, key, value):
        cache_node = self._dict[key]
        cache_node._value = value
        self._updateCacheNodeOrder(key, cache_node)        
     
    def _putNew(self, key, value):
        cache_node = None
        if self._qsize == self._capacity:
            cache_node = self._qhead
            self._qhead = self._qhead._next
            self._qhead._prev = None
            del self._dict[self._qhead._key]
            cache_node._key = key
            cache_node._value = value
        else:
            self._qsize += 1
            cache_node = CacheNode(key, value)
        self._insertCacheNode(key, cache_node)
        
    def put(self, key, value):
        if key in self._dict:
            self._putExisting(key, value)
        else:
            self._putNew(key, value)