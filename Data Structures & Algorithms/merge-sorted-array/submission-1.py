class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = m + n - 1 # Last slot of nums1
        p1 = m - 1 # index Last element of nums1
        p2 = n - 1 # index Last element of nums2 

        # while index left, compare end values and add largest values to end of nums1, then move one step back in that array 
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 = p1 - 1
            elif nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 = p2 - 1 

            p = p - 1
            
        # If nums1 array ends before nums2, still need to move leftovers of other
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 = p2 - 1 
            p = p - 1


        """
        Do not return anything, modify nums1 in-place instead.
        """
        