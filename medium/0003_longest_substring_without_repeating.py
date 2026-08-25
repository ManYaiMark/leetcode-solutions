class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # index_s = 0
        L = 0
        max_s = 0  
        # R = 0
        # max_chr = 0
        seen = set()
        
        # print(len(s))
        for R in range(len(s)):
            
            while s[R] in seen :
                seen.remove(s[L])
                L += 1
            
            
            seen.add(s[R])

            max_s = (R - L) + 1 if (R - L) + 1 >= max_s else max_s
            # print(max_s)
        
        return max_s