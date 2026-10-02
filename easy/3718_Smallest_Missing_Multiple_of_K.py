class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            if k * (i + 1) not in nums:
                return k * (i + 1)
        return k * (i + 2 )  
