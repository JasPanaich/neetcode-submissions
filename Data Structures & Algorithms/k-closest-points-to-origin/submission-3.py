class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use minHeap: gives smallest elemet first so insert into minHeap
        minHeap = [] # Initially, minheap is an array

        # Go through every point and compute distance
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            # append point to minheap, with distance first b/c its the key-value 
            minHeap.append((dist, x, y))

        heapq.heapify(minHeap) # Reorders list to make sure its in structure of heap
        res = []

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1 

        return res

        # O(N + KlogN) time complexity 

        