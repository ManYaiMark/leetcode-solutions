class Solution:
    """
    โจทย์: กำหนดอาร์เรย์ nums และจำนวนเต็ม l, r ให้หา subarray ที่มีความยาวตั้งแต่ l ถึง r และมีผลรวมมากกว่า 0 
    จากนั้นคืนค่าผลรวมที่น้อยที่สุดที่เป็นไปได้ หากไม่มี subarray ที่ตรงเงื่อนไขให้คืนค่า -1

    วิธีคิด
    หา subarray แล้วก็เช็คว่าเข้าเงื่อนไขไหม ถ้าเข้าก็เช็คว่าน้อบสุดไหม
    """
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:    
        n = len(nums)
        min_sum = None
        for i in range(n):
            for j in range(i+1 ,n+1):
                # m = len(nums[i:j])
                m = nums[i:j]
                if len(m) >= l and  len(m) <= r:
                    s = sum(m)
                    if s > 0:
                        if min_sum is None or s < min_sum:
                            min_sum = s
        if min_sum :
            return min_sum
        return -1
            