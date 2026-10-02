class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy()) # Need curr for other cases, so just use one copy 
                return

            # Can't find combination
            if i >= len(nums) or total > target:
                return 

            # Recursive step
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()

            # Can't include candidate
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res


                        
        