class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        """
        โจทย์: กำหนดอาร์เรย์ arr1, arr2 และจำนวนเต็ม d ให้นับจำนวนสมาชิกใน arr1 ที่มีระยะห่างจากสมาชิก ทุกตัว ใน arr2 มากกว่า d โดยระยะห่างคำนวณจาก |arr1[i] - arr2[j]|

        วิธีคิด
        +=1 ก่อนเข้า loop ไล่หาทุกกรณีที่ไม่นับแล้วค่อย -= 1 ใช้ break เพื่อทำให้ไวขึ้น
        """
        total = 0
        for i in range(len(arr1)):
            total += 1
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d :
                    total -= 1
                    break
        return total