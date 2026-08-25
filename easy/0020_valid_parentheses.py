class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        seen = []

        for i in range(len(s)):

            if s[i] in pairs and len(seen) > 0:
                last = seen[-1]
                if pairs[s[i]] == last:
                    seen.pop()
                else :
                    seen.append(s[i])
            else :
                seen.append(s[i])

            return len(seen) == 0

        return False
