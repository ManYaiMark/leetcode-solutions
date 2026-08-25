class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = 0

        while n < len(s) -1 :
            num1 = roman[s[n]]
            num2 = roman[s[n+1]]

            if num1 < num2 :
                total -= num1
            else :
                total += num1  
            n += 1
        total += roman[s[-1]]
        return total
