class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Set 2d grid initially to all 0's
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)] # +1 since we need col for zeros

        # Nested loop to iterate over 2d grid in reverse
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1] # Characters matched, so add 1 to it and move diagonally
                else:
                    # If they dont match...get max of value below or to the right
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        return dp[0][0] # Result at top left

        