class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        ma, da = map(int,arriveAlice.split("-"))
        mla, dla = map(int,leaveAlice.split("-"))
        
        mb, db = map(int,arriveBob.split("-"))
        mlb, dlb = map(int,leaveBob.split("-"))
        # จำนวนวันในแต่ละเดือนที่โจทย์กำหนด (not a leap year)
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # หาวันที่ในปีนั้นๆ เช่น 03-25 จะเท่ากับ 31 + 28 +25
        sa = sum(months[:ma-1]) + da
        la = sum(months[:mla-1]) + dla

        sb = sum(months[:mb-1]) + db
        lb = sum(months[:mlb-1]) + dlb

        start = max(sa,sb)
        end = min(la,lb)

        # สามารถใช้ > เปรียบเทีบ str ได้ เพราะเป็น M-D และมีการเพิ่ม 0 หน้าเดือนที่เป็นตัวเดียว 
        # จะทำให้ตัดโค้ดไวเพราะสามารถนำไปใช้ด้านบนกรอง testcase ที่เป็น 0 ได้เร็วขึ้น
        if start > end :
            return 0

        return end - start + 1