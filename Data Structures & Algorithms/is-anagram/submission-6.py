class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        # Count up for s and down for t at the same time since we checked they are the same length
        for i in range(len(s)):
            # Use .get so if key DNE yet, it defaults to 0 value
            count[s[i]] = (count.get(s[i], 0)) + 1
            count[t[i]] = (count.get(t[i], 0)) - 1

        
        for val in count.values(): # Returns count of values only
            if val != 0: # Since they should all be 0 out if anagram
                return False 
    
        # If loop successfully checks all
        return True 


        