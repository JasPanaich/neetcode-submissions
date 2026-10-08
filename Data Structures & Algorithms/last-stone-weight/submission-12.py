import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Put stones in max heap
        # Putting each stone in list and multiplying by -1 so the largest value is the smallest -> so when we make min heap it is actually a max heap
        new_stones = []
        for stone in stones:
            new_stones.append(-stone)

        heapq.heapify(new_stones) # Creating the heap

        while len(new_stones) > 1:
            first_largest = heapq.heappop(new_stones)
            second_largest = heapq.heappop(new_stones)

            if first_largest < second_largest:
                new_weight = first_largest - second_largest

                # Put stone back in heap
                heapq.heappush(new_stones, new_weight)

            
        if (len(new_stones) == 0):
            return 0
        else:
            return new_stones[0] * -1

        