class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {} # value -> index 
        # Enumerate keeps track of index and value which is needed in this question 
        # First loop to append elements, keeping order
        for i, n in enumerate(nums): # i is index and n is value
            diff = target - n 
            if diff in results:
                return [results[diff], i]

            results[n] = i
