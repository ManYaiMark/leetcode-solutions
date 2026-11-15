class Solution:
    """
    โจทย์: กำหนดอาร์เรย์จำนวนเต็ม nums ให้หาความยาวของ subarray ที่ยาวที่สุด 
    ซึ่งสมาชิกเรียงเพิ่มขึ้นอย่างเคร่งครัดหรือลดลงอย่างเคร่งครัด โดยสมาชิกใน subarray ต้องอยู่ติดกัน และค่าที่อยู่ติดกันห้ามเท่ากัน

    วิธีคิด
    ตอนแรกใช้การหา subarray แล้วใช้ loop เยอะทำให้ช้า แม้โจทย์มีข้อไม่มาก
    เลยเปลียนไปใช้การ loop ครั้งเดียว แต่ทำการใช้ if ให้คุมทุกกรณี แต่โค้ดยังต้องปรับอีก แต่ตอนนี้พอใจแค่นี้
    """
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 :
            return 1
        mres = 0
        # โค้ดขั้นแรก ลองทำให้ได้ผลลัพ ตามโจทย์ก่อน
        # for i in range(n):
        #     for j in range(i+1,n+1):
        #         res = 1
        #         l = ''
        #         m = nums[i:j]
        #         for k in range(1,len(m)):
        #             if m[k] > m[k-1] and l in ('>', ''):
        #             # if nums[i:j][k] > nums[i:j][k-1] and l == '>' or nums[i:j][k] > nums[i:j][k-1] and l == '':  
        #                 l = '>'
        #                 res += 1
        #             elif m[k] < m[k-1] and l in ('<', ''):  
        #             # elif nums[i:j][k] < nums[i:j][k-1] and l == '<' or nums[i:j][k] < nums[i:j][k-1] and l == '':  
        #                 l = '<'
        #                 res += 1
        #             else :
        #                 mres = max(res,mres)
        #                 break
        #             mres = max(res,mres)
        # return mres
        
        # แล้วค่อยปรับปรุงให้สามารถทำได้ไวขึ้น
        h = ''
        res = 1
        for k in range(1,len(nums)):
            if nums[k] > nums[k-1] and h in ('>', ''):
                h = '>'
                res += 1
            elif nums[k] < nums[k-1] and h in ('<', ''):  
                h = '<'
                res += 1
            else :
                mres = max(res,mres)
                res = 1
                if nums[k] > nums[k-1] :
                    h = '>'
                    res += 1
                elif nums[k] < nums[k-1] :
                    h = '<'
                    res += 1
                continue
            mres = max(res,mres)
        return mres