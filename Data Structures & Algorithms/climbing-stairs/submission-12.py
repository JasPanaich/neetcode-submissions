class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1 # Ways to reach current top
        two = 1 # Ways to reach previous step

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one        