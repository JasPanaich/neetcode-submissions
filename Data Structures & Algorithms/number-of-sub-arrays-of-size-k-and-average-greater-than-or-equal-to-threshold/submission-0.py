class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = 0
        count = 0
        L = 0

        for R in range(len(arr)):
            window_sum += arr[R]

            if R - L + 1 > k:
                window_sum -= arr[L]
                L += 1

            if (R - L + 1 == k) and (window_sum/k >= threshold):
                count += 1

        return count


                
        