class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert kth largest to the corresponding 0-based sorted index
        target_idx = len(nums) - k 
         
        def quickSelect(l, r):
            pivot, p = nums[r], l  # Use variable 'l' as the lower bound
             
            for i in range(l, r):  #  Iterate from 'l' up to 'r'
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                         
            # Swap pivot value with p index (middle)
            nums[p], nums[r] = nums[r], nums[p]
             
            # Did we find the solution?
            if p > target_idx:
                return quickSelect(l, p - 1)  # Bug fix: Search left partition up to p - 1
            elif p < target_idx:
                return quickSelect(p + 1, r)  # Search right partition from p + 1
            else: 
                return nums[p]
         
        return quickSelect(0, len(nums) - 1)