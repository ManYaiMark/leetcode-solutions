class Solution:
    # โจทย์
    '''
    You are given an array of integers nums.
    Choose two different indices i and j of that array.
    Return the maximum value of (nums[i] - 1) * (nums[j] - 1).
    
    แนวทางการแก้ :
    หาว่าต่ำแหน่งไหนมีค่าสูงสุดใน list โดยห้ามซ้ำกัน
    '''
    def maxProduct(self, nums: list[int]) -> int:
        # ถ้า len = 2 คือไม่ต้องหาให้เสียเวลา
        if len(nums) == 2 :
            return (nums[0] - 1) *( nums[1] - 1)
        # กำหนดต่ำแหน่งเป็น -1 จะได้ไม่ซ้ำกับต่ำแหน่งอื่น
        mi = -1
        mj = -1
        # หาว่าต่ำแหน่งไหนเยอะสุด จริงน่าจะใช้ nums.index(max(nums))) ได้ แต่เขียนเองเลยน่าจะง่ายกว่า
        for i in range(len(nums)):
            if nums[i] >= nums[mi] :
                mi = i
        # หาเหมือนเดิม
        for j in  range(len(nums)):
            # แต่ถ้าซ้ำกับตำแหน่งเดิมก็ข้าม
            if mi == j :
                continue
            if nums[j] >= nums[mj] :
                mj = j
        # return ตามโจทย์ คุณสมบัติการคูณสลับหน้าหลังได้
        return (nums[mi] - 1) *(nums[mj] - 1)
