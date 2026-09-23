class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x 
        if target == 0 :
            return n
        elif n ==  1 :
            return -1 

        left = 0
        right = 0 
        sumN = 0
        maxLength = 0

        while  right < n  :
            sumN += nums[right]
            right += 1

            while sumN > target and left < n :
                sumN -= nums[left]
                left += 1


            if sumN == target :
                maxLength = max((right-left),maxLength)

        if maxLength == 0 :
            return -1

        return n - maxLength 
