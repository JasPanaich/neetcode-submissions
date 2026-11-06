class Solution:
    def rob(self, nums: List[int]) -> int:
        # Initialized at 0 in case we get an empty subarray
        rob1 = 0 # House before rob2
        rob2 = 0 # Last house we robbed

        # Iterating through each of the houses we can rob
        # [rob1, rob2, num, num + 1]
        for num in nums:
            # Compute max we can rob up until this current house
            temp = max(num + rob1, rob2) # Rob this house (add to total from 2 houses back), or skip house (keep previous total)
            # Shift one house down the street
            rob1 = rob2 
            rob2 = temp # Rob 2 is now best total

        return rob2 # Rob2 is equal to last value  
        