class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2

        while i >= 0:

            if nums[i] < nums[i+1] :
                L = i + 1
                j = 1
                R = len(nums) - 1
                    
                while j < len(nums) :
                    if nums[-j] > nums[i] :
                        nums[i] ,nums[-j] = nums[-j] ,nums[i]

                        while L < R :
                            # if nums[L] > nums[R] :
                            nums[L] ,nums[R] = nums[R] , nums[L]
                            L += 1
                            R -= 1
                        return
                    j += 1
            i -= 1

        L = 0
        R = len(nums) - 1
        while L < R :
            # if nums[L] > nums[R] :
            nums[L] ,nums[R] = nums[R] , nums[L]
            L += 1
            R -= 1


