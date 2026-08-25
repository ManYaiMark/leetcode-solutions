class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        single_int = int("".join(map(str, digits)))
        single_int += 1
        int_list = [int(x) for x in str(single_int)]
        return int_list