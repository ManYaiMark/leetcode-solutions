class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1

        num = int(str(abs(x))[::-1]) * sign

        if num < -2147483648 or num > 2147483647 :
            return 0
        
        return num