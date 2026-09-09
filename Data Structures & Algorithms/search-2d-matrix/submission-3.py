class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 

        rows = len(matrix)
        columns = len(matrix[0])
        right = (rows * columns) - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // columns
            column = mid % columns

            if target > matrix[row][column]:
                left = mid + 1
            elif target < matrix[row][column]: 
                right = mid - 1
            else:
                return True
        return False


        