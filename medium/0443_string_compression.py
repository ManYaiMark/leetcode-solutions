class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1 :
            return 1
        result = ''
        # แปรงเป็น str เพื่อให้ง่ายต่อการจัดการ
        result_empty = "".join(chars)
    
        count = 1
        k = 0

        for i in range(1,len(result_empty)):
            if result_empty[i] == result_empty[i-1]:
                count += 1
            # กันในกรณีที่มีตัวเดียว
            elif count == 1 :
                chars[k] = result_empty[i-1]
                k += 1
            # นำข้อมูลเข้าไปแก้ไขใน list เดิม
            else :    
                chars[k] = result_empty[i-1]
                k += 1
                for digit in str(count):
                    chars[k] = digit
                    k += 1

                count = 1
        # end ควรจะเขียนเป็น def เพราะใน loop ก็มีแล้วอันหนึ่ง
        if count == 1 :
            chars[k] = chars[-1]
            k += 1
        else :
            chars[k] = chars[-1]
            k += 1
            for digit in str(count):
                chars[k] = digit
                k += 1
            
        # ทำให้ list มีถึงแค่ k 
        chars[:] = chars[0:k]

        return k
