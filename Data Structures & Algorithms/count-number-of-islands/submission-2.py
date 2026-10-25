class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 # If grid empty

        # Get dimensions of grid
        rows, cols = len(grid), len(grid[0])

        # Mark positions as already visited
        visited = set()

        islands = 0 # Need to count num of islands

        # Bfs so we can look at positions in grid next to current one
        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c)) # Add cell that we call this on to visted
            q.append((r, c))

            # While q not empty, keep exanding island 
            while q:
                row, col = q.popleft()
                # Want to check adjacent positions of the one we popped
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    # neighbor_row = row + dr
                    # neighbor_col = col + dc
                    # Checking if in bounds and not visited
                    if ((row + dr) in range(rows) and (col + dc) in range(cols) and grid[row + dr][col + dc] == "1" and (row + dr, col + dc) not in visited):
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))
        
        # Want to visit every single position in grid, so iterate through every row and col
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands