class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dp(grid):
            rows, cols = len(grid), len(grid[0])
            prevRow = [0] * cols

            for r in range(rows - 1, -1, -1):
                curRow = [0] * cols

                for c in range(cols - 1, -1, -1):
                    if grid[r][c] == 1:
                        curRow[c] = 0  # obstacle: no paths through here
                    elif r == rows - 1 and c == cols - 1:
                        curRow[c] = 1  # destination
                    else:
                        right = curRow[c + 1] if c + 1 < cols else 0
                        curRow[c] = right + prevRow[c]

                prevRow = curRow  # once per row, after the inner loop

            return prevRow[0]  # top-left value

        return dp(obstacleGrid)