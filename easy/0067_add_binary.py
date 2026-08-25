class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = -1
        carry = 0

        nums = ""

        max_str = max(a,b, key=len)
        min_str = min(b,a, key=len)

        if len(max_str) != len(min_str):
            i = len(max_str) - len(min_str)
            min_str = ("0" * i) + min_str 

        while len(max_str) + n  >= 0:
            
            num = int(max_str[n]) + int(min_str[n]) + carry

            if num >= 2 :
                nums = str(num % 2) + nums 
                carry = num // 2 
                n -= 1
            else :
                nums = str(num % 2) + nums 
                carry = num // 2 
                n -= 1

        if carry >= 1 :
            nums = str(carry) + nums

        return  nums
