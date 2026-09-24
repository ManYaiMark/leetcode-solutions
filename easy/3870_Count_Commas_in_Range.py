class Solution:
    def countCommas(self, n: int) -> int:
        if len(str(n)) < 4 :
            return 0

        return n - 1000 + 1