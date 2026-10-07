class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # กรณีมีใน list ตัวเดียว
        n = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i] - 1 :
                # บวกเพิ่มหากเป็น perfix
                n += nums[i]
            else :
                # ออกหากไม่มี
                break
        # เช้คว่ามีใน nums ไหม ถ้ามีก็ + 1 เพื่อให้ไม่มี
        while n in nums :
            n += 1
        return n 