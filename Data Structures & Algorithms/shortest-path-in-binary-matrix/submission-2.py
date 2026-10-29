class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid) # Square, so rows and col are same      
        q = deque([(0, 0, 1)]) # row, column, length
        visit = set([(0, 0)]) # Keep track of positions visited
        # Directions that can be visited (8 options)
        direct = [[0,1],[1,0],[0,-1],[-1,0],[-1,-1],[1,1],[-1,1],[1,-1]]

        while q:
            r, c, length = q.popleft()
            # Make sure it is valid
            if (r < 0 or c < 0 or r == N or c == N or
            grid[r][c] == 1):
                continue # If any true, skip this position
            # If we have reached result 
            if r == N - 1 and c == N - 1:
                return length
            
            # Go through all of the neighbors of this position
            for dr, dc in direct:
                if (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))
        return -1

        