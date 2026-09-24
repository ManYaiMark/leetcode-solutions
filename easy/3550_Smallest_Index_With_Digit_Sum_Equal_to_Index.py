class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        def sumDigits(num):
            x = 0
            for i in str(num):
                x += int(i)
            return x
            
        s = 1001
        for i in range(len(nums)):
            if sumDigits(nums[i]) == i :
                return i
    

        return -1
