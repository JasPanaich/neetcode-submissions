import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.heap = [] # min-heap holding largest k value seen
        for num in nums:
            self.add(num) # Get starting numbers into the heap

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val) # Not full yet so push it
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val) # Pop root, push val
        return self.heap[0] # Root = kth largest
        
