class Solution:
    """
    โจทย์: กำหนดอาร์เรย์ String patterns และ String word ให้นับจำนวน String ใน patterns ที่ปรากฏเป็น substring อยู่ใน word 
    โดย substring ต้องเป็นตัวอักษรที่อยู่ติดกัน และหากมี pattern ซ้ำกันให้แต่ละตัวถูกนับแยกกัน

    วิธีคิด 
    ตอนแรกใช้ in เพระคิดไม่ออกว่าทำยังไง ไวกว่าแบบที่สองที่คิดขึ้นมาด้วย
    แบบที่สองใช้การ loop และเช็คแบบ slicing ไปเลื่อยๆ
    hard code กว่า แต่ก็ทำให้เข้าใจว่าอันกอลิทึมมากกว่า
    """
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        total = 0
        # for i in patterns :
        #     if i in word :
        #         total += 1
        # return total
        for pattern in patterns:
            # len word - len pattern + 1 จะทำให้ไม่ index out of range +1 เพราะ index เริ่มที่ 0 จบลงด้วย เลขหลัง -1
            for i in range(len(word)-len(pattern)+1):
                if word[i : i + len(pattern)] == pattern:
                    total += 1
                    # ใช้ break เพื่อที่จะไม่ให้หาต่อ หากเจอแล้ว
                    break
        return total