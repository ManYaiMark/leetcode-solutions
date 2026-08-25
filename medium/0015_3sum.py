class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3 :
            return []

        list_n = []
        nums.sort()

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = len(nums) - 1

            while L < R:
                if nums[L] + nums[R] == -nums[i] :
                    list_n.append([nums[i], nums[L], nums[R]])
                    
                    while L < R and nums[L] == nums[L+1]: L += 1
                    while L < R and nums[R] == nums[R-1]: R -= 1    
                    
                    R -= 1
                    L += 1
                elif nums[L] + nums[R] > -nums[i] :
                    R -= 1
                elif nums[L] + nums[R] < -nums[i] : 
                    L += 1

        return list_n