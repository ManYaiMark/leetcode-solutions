class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        replace = s.split()

        return len(replace[-1])

