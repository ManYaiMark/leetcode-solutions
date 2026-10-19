class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        n = []
        nums.sort()
        for i in range(len(nums)) :
            if nums[i] == target :
                n.append(i)
        return n