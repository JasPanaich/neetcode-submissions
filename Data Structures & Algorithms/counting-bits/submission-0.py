class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1) # How many trying to compute
        offset = 1 # Highest power of 2 so far

        for i in range(1, n + 1):
            # Can we double offset
            if offset * 2 == i: 
                offset = i
                # Number of 1 bits in each int binary rep
            dp[i] = 1 + dp[i - offset]

        return dp

        


        