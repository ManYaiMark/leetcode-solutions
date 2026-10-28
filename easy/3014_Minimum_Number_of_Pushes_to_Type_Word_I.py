class Solution:
    def minimumPushes(self, word: str) -> int:
        # ถ้าน้อยกว่าหรือเท่ากับ 8 คือเป็น 8 แน่นอน จริงถ้ารู้แต่แรกว่าไม่ซ้ำคงได้ใช้หลักคณิตศาสตาร์แก้ข้อนี้แน่นอน
        if len(word) <= 8 :
            return len(word)

        # ตอนแรกนึกว่าคำใน word ซ้ำได้เลยสร้างเป็น dict ไว้เก็บ 
        seen = dict()
        total = 0
        n = 1
        for i in range(len(word)):
            j = word[i]
            # ถ้าไม่มีให้เพิ่ม
            if j not in seen:
                seen[j] = n
                total += n
            
            else :
                # ถ้ามีให้ total + ด้วย n ที่เพิ่มไปก่อนหน้านี้
                total += seen[j]

            # โจทย์จำกัดที่ 8 เลข เลยทำการเพิ่มที่ละ 8 แต่เรียงลงเพราะตอนแรกใช้ > เลยทำให้มันบัค
            if len(seen) == 24 :
                n = 4
            elif len(seen) == 16 :
                n = 3
            elif len(seen) == 8 :
                n = 2

        return total
    

        '''
        # โจทย์บอกว่า word ไม่ซ้ำ เลยทำให้ได้วิธีแก้แบบใหม่
        total = 0
        n = 1

        for i in range(len(word)):
            total += n
            # index + 1 จะได้จำนวนเลขที่ถูกบรรทึกไปแล้ว
            if (i + 1) % 8 == 0:
                n += 1

        return total'''