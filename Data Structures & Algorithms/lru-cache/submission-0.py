# Create node class so that it can keep track of last/least used
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        # Two pointers, for prev and next nodes, initially not pointing at anything
        self.prev = None
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        # Capacity needs to be stored so we'd know if we went over capacity
        self.cap = capacity
        self.cache = {} # Map key to node 

        # Dummy nodes telling us least and most recent values added
        self.left = Node(0,0)
        self.right = Node(0,0)
        # Left=LRU, right= most recent
        # Initially want to connect the nodes 
        self.left.next = self.right
        self.right.prev = self.left
        
    # Helper function so we can remove node
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # Helper function so we can add node that was just added to cache 
    # Insert right 
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        # If the key exist in cache, return value (from a node) 
        if key in self.cache:
            # Update to most recently used now
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 # If DNE

    def put(self, key: int, value: int) -> None:
        # If we have a key in cache, node already exist in list with that key so remove it
        if key in self.cache:
            self.remove(self.cache[key])
        # Create new node with the key value pair, and place in hashmap so node can be found fast
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key]) # Insert into list to keep track of order (most recent)

        if len(self.cache) > self.cap:
            # Remove from list and delete LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] # Del removes references

        
