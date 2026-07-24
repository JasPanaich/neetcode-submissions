class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak_counter = 0
        maximum_streak = 0
        
        for num in nums: 
            if num == 1:
                streak_counter += 1 
                if (streak_counter > maximum_streak):
                    maximum_streak = streak_counter
            elif num != 1: 
                streak_counter = 0 
        return maximum_streak 

        
        