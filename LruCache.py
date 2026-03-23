from collections import OrderedDict

class LRU:
    """Least Recently Used (LRU) Cache implementation using OrderedDict.
    
    Maintains a fixed-capacity cache where the least recently used items
    are evicted when capacity is exceeded.
    """
    
    def __init__(self, cap):
        """Initialize LRU cache with given capacity.
        
        Args:
            cap: Maximum capacity of cache (must be positive integer)
        
        Raises:
            ValueError: If cap is not a positive integer
        """
        if not isinstance(cap, int) or cap <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.cache = OrderedDict()
        self.cap = cap

    def get(self, key):
        """Retrieve value for key and mark as recently used.
        
        Args:
            key: Key to retrieve
        
        Returns:
            Value associated with key, or -1 if not found
        """
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, val):
        """Insert or update key-value pair and mark as recently used.
        
        If cache is full, evicts least recently used item.
        
        Args:
            key: Key to insert/update
            val: Value to store
        """
        if key in self.cache:
            # update existing key and mark as recently used
            self.cache[key] = val
            self.cache.move_to_end(key)
            return

        if len(self.cache) >= self.cap:
            # evict least recently used (first item)
            self.cache.popitem(last=False)

        self.cache[key] = val

    def delete(self, key):
        """Remove a key from cache.
        
        Args:
            key: Key to delete
        
        Returns:
            True if key was deleted, False if key not found
        """
        if key in self.cache:
            del self.cache[key]
            return True
        return False

    def display(self):
        """Display current cache contents in order (most recently used last)."""
        if not self.cache:
            print("Cache is empty")
            return
        items = ", ".join(f"{k}: {v}" for k, v in self.cache.items())
        print(f"Cache [{len(self.cache)}/{self.cap}]: {items}")

    def __repr__(self):
        items = ", ".join(f"{k}: {v}" for k, v in self.cache.items())
        return f"LRU(cap={self.cap}, items=[{items}])"

    def __len__(self):
        return len(self.cache)