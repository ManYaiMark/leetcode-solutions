class Solution:
    def reverseDegree(self, s: str) -> int:
        t = 0
        for i in range(len(s)):
            t += (i+1) * (123-ord(s[i]))

        return t