class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = str(n)
        if len(num) <= 1:
            return False
        
        total_sum = 0
        total_p = 1
        for i in range(len(num)):
            total_sum += int(num[i])
            total_p *= int(num[i])
        
        return n % (total_sum + total_p) == 0