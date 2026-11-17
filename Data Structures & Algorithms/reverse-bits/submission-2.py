class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Append n lowest bit to result
            result = (result << 1) | (n & 1) # | bitwise or operator
            n >>= 1      # Move to next bit of n
        return result
