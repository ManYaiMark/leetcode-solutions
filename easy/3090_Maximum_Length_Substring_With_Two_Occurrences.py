class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        L = 0
        R = 0
        m = 0
        count = {}

        while R < len(s):
            # get count of s[R] in count if not = 0 + 1 if have + 1
            count[s[R]] = count.get(s[R], 0) + 1
            while count[s[R]] > 2:
                
                count[s[L]] -=  1
                L += 1
            
            R += 1
            m = max(m,R - L)


        return m 
