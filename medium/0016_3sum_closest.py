class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        if len(nums) < 3 :
            return []

        closest_num = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = len(nums) - 1

            while L < R:
                sum_n = nums[L] + nums[R] + nums[i]
                
                if abs(sum_n - target) < abs(closest_num  - target) :
                    closest_num  = sum_n

                if sum_n == target :
                    return target
                elif sum_n  < target :
                    L += 1
                elif sum_n > target : 
                    R -= 1

        return closest_num 