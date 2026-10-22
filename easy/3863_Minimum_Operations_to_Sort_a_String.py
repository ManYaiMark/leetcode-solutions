class Solution:
    def minOperations(self, s: str) -> int:
        # ทำให้ตัวหนังสือสามารถ sort ได้
        n = []
        for i in s:
            n.append(ord(i))

        # เช็คว่า sort ไหม ถ้าใช่คือ 0
        if n == sorted(n):
            return 0
        # โจทย์บอกว่าห้ามเลือกทั้งหมด ดังนั้น 1,2 จึงต้อง return -1
        if len(s) <= 2 and n != sorted(n):
            return -1
        # หาว่า min,max อยู่ index ไหน
        min_c = 0
        max_c = 0
        for i in range(len(s)):
            if s[i] < s[min_c]:
                min_c = i
            if s[i] >= s[max_c]:
                max_c = i
        # ถ้า min อยู่หน้า หรือ max อยู่หลัง หมายถึงเลือกได้ทุกตัว -1 แล้วเรียง 
        if min_c == 0 or max_c == len(s)-1:
            return 1
        # ถ้า min อยุ่หลัง max อยู่หน้า จะสามารถสลับได้มากขึ้น เพราะ
        if min_c == len(s)-1 and max_c == 0:
            return 3
        # หากไม่ต้องสักข้อ return 2 
        return 2
