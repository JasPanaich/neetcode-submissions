class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # Set filters out duplicates, so if equal, that means theres no duplicates
        if len(nums) == len(set(nums)): 
            return False
        else:
            return True
        