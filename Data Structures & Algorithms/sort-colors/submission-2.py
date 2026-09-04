class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0, 0, 0]

        # Count quantity of each value in array
        for num in nums:
            counts[num] += 1

        i = 0
        for n in range (len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1 
        
        