class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        r = 1
        # สามารถแทนโดย True แล้วก็เอา r = 1 ออกด้วย
        while r != 0:
            # เป็น 1 เพื่อที่จะได้ * ได้
            total = 1
            for i in str(n) :
                total *= int(i)
            # หาว่าหารลง ตัวยัง
            r = total % t 
            if r == 0 :
                return n
            # เพิ่มทีละ 1 เพื่อเช็คทุก subarray
            n += 1
        return n