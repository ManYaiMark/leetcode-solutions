class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # เก็บค่าที่เคยเห็น 
        seen = {}
        for i,num in enumerate(nums):
            # จำนวนที่ขาดไปจนกว่าจะถึง target
            complement = target - num 
            # เช็คว่ามีตัวที่ขาดไปที่เคยเจอว่ามีมีตัวไหนเท่ากันไหม
            if complement in seen :
                return [seen[complement],i]
            # เก็บค่าที่เคยเห็นเป็น ตัวเลข, index
            seen[num] = i
