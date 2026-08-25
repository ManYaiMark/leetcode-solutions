class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1 :
            return 2147483647
            
        if divisor == 1 :
            return dividend
        elif divisor == -1 :
            return -dividend

        ngt = 1
        if dividend < 0 or divisor < 0:
            ngt = -1
            if dividend < 0 and divisor < 0:
                ngt = 1
        
        ans = 0
        dividend  = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            n = 0
            while dividend >= (divisor << (n + 1)):
                n += 1
            
            dividend -= (divisor << n)
            ans += (1 << n)
            
        if ngt < 0 :
            return -ans

        return ans
