class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        result = right # Max solution can be

        while left <= right:
            k = (left + right) // 2
            hours = 0 # How many hours to eat all bananas
            for pile in piles:
                hours += math.ceil(pile / k) # Have to round up since whole bananas only

            if hours <= h:
                result = min(result, k)
                right = k - 1 
            else:
                left = k + 1 
            
        return result 

        