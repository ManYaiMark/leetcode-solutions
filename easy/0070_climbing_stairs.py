class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev1 = 1
        prev2 = 2

        if n == 1:
            return prev1  
        if n == 2 :
            return prev2  

        for i in range(n-2):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current

        return current