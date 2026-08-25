class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if s == "":
            return 0
        INT_MIN = -2147483648
        INT_MAX = 2147483647

        result = ""
        sign = 1
        
        
        if "-" == s[0]:
            s = s[1:]
            sign = -1
        elif "+" == s[0]:
            s = s[1:]

        for i in range(len(s)):
            if s[i].isdigit() :
                result += s[i]
            else :
                break
        
        if result == "":
            return 0
        result = int(result) * sign
        

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result