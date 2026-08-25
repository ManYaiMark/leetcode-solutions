class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        def expand(l, r):
            if l < 0 or r >= len(s) or s[l] != s[r]:
                return s[l+1:r]
            return expand(l-1,r+1)
                
        i = 0
        result = []

        if len(s) == 1 :
            return s

        while i >= 0 and i < len(s) :
            odd  = expand(i, i)
            even = expand(i, i+1) 

            i += 1
            result.append(max(odd, even, key=len))

        return max(result,key=len)