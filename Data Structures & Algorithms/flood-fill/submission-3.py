class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc] # Store original color of starting pixel
        if orig == color:
            return image # Already the right color

        # Perform dfs to change color of visited pixels that are connected
        row = len(image) 
        column = len(image[0])

        def dfs(r, c):
        # If out of bounds, or pixel does not match original
            if r < 0 or r >= row or c < 0 or c >= column or image[r][c] != orig:
                return 

            # Otherwise, change pixel to new color and call on neighbors
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr, sc) # Call on the parameters
        return image
