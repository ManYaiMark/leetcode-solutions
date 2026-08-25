class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_list = sorted(strs, key=len)
        first = min_list[0]
        total = ""

        for i in range(len(first)):

            char = first[i]
            
            for word in strs:
                if char != word[i] :
                    return total
            
            total += char

        return total
