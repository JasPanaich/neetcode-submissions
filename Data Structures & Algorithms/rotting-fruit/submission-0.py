class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Multisource BFS
        q = deque()
        time = 0 # Keep track of how much time has passed
        fresh = 0 # Keep track of how many fresh oranges we have

        ROWS, COLS = len(grid), len(grid[0])
        # Iterate over entire grid
        for r in range(ROWS):
            for c in range(COLS):
                # Counting num of fresh oranges
                if grid[r][c] == 1:
                    fresh += 1
                # Identify rotting oranges
                if grid[r][c] == 2:
                    q.append([r,c]) # Appending coordinates
        
        # Variable of adjacent spots to fresh orange
        directions = [ [1,0],[0,1],[-1,0],[0,-1] ]
        
        while q and fresh > 0:
            # Pop fresh oranges
            for i in range(len(q)):
                r, c = q.popleft()
                # Go to adjacent spots of orange
                for dr, dc in directions:
                    row, col = dr + r, dc + c # Adjacent spots
                    # If in bounds and fresh, make rotten
                    if (row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2 # Turn rotten
                    q.append([row, col]) # Include this to rot others in next iteration
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1 

        