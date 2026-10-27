class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # If grid empty
        if not grid:
            return 0 

        # Get length of rows and cols
        rows = len(grid)
        cols = len(grid[0]) 

        # Mark positions as already visited so we don't recheck them
        visited = set()


        
        # DFS so we can look at positions of grid
        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0 or (r,c) in visited:
                return 0

            visited.add((r,c))

            # Recursive call + 1 to count the current cell
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) 

        max_area = 0


        # Start dfs from every cell
        for r in range(rows):
            for c in range(cols):
                max_area = max(max_area, dfs(r,c)) # Best so far vs one we just measured

        return max_area
            
                

        