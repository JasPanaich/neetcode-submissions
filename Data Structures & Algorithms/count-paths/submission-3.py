class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(rows, cols):
            prevRow = [0] * cols

            for r in range(rows - 1, -1, -1):
                curRow = [0] * cols
                curRow[cols - 1] = 1 # Assigns 1 to last row of array
                for c in range(cols - 2, -1,-1):
                    curRow[c] = curRow[c + 1] + prevRow[c]
                prevRow = curRow

            return prevRow[0] # Return top left val

        
        return dp(m,n)