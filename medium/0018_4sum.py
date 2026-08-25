class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4 :
            return []

        list_n = []
        nums.sort()


        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target :break
            
            for j in range(i+1,len(nums) - 2) :
                if i != j-1 and nums[j] == nums[j-1]:
                    continue
                    
                L = j + 1
                R = len(nums) - 1

                t = target - nums[i] - nums[j]

                while L < R:
                    s = nums[L] + nums[R]
                    if s  == t :
                        list_n.append([nums[i],nums[j], nums[L], nums[R]])
                        
                        while L < R and nums[L] == nums[L+1]: L += 1
                        while L < R and nums[R] == nums[R-1]: R -= 1    
                        
                        R -= 1
                        L += 1
                    elif s  > t:
                        R -= 1
                    elif s  < t: 
                        L += 1
                

        return list_n