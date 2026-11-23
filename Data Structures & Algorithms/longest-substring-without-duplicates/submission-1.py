class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        longest = 0 
        seen = set()

        for R in range(len(s)):
            
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
                
            longest = max(longest, R - L + 1)
            # Add the right pointer after checking
            seen.add(s[R])
        
        return longest





        