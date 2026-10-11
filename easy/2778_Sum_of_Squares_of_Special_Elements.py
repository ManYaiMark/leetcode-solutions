class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(n):
            if n % (i+1) == 0 :
                total += nums[i] * nums[i]
        return totalv