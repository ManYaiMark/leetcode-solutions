class Solution:
    def countCommas(self, n: int) -> int:
        len_n = len(str(n)) 
        if len_n < 4 :
            return 0

        total = 0
        # loop ทุกหลัก
        for i in range(4,len_n+1) :
            comma = (i - 1) // 3
            # เช็คว่าเกินหลักสุดท้ายยัง
            if n >= (10**i-1) :
                total += ((10 ** i) - 1 - (10**(i-1)) + 1) * comma
            
            else :  
                total += (n - (10**(i-1)) + 1) * comma
                return total

        # total += (จุดสิ้นกลุ่ม - จุดเริ่มกลุ่ม + 1) × comma_ต่อตัว
        # total += (n - จุดเริ่มกลุ่ม + 1) × comma_ต่อตัว

        return total