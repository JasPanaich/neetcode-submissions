class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(index):
            if index >= len(nums): # If index is out of bounds
                res.append(subset.copy()) 
                return 

            # Decision to include nums[index]
            subset.append(nums[index])
            dfs(index + 1)

            # Decision NOT to include nums[index]
            subset.pop() # Empty subset given to it
            dfs(index + 1) 

        dfs(0)
        return res
        