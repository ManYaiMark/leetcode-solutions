class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        for i in range(n):
            for j in range(i+1,n+1):
                total += (len(set(nums[i:j])))**2
                
        return total