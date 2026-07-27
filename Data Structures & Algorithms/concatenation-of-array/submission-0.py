class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Create new array double the capacity
        ans = nums
        nums = 2 * ans
        newArr = [0] * len(nums)

        # Copy elements into newArr
        for i in range(len(newArr)):
            newArr[i] = nums[i]
            ans = newArr
        return ans
