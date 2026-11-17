class Solution:
    """
    โจทย์: กำหนดจำนวนเต็ม n ให้หาผลรวมของเลขคี่บวก n ตัวแรก (sumOdd) 
    และผลรวมของเลขคู่บวก n ตัวแรก (sumEven) จากนั้นคืนค่า ห.ร.ม. (GCD) ของ sumOdd และ sumEven

    วิธีคิด
    จริงๆข้อนี้ return n ไปเลยก็ได้ เพราะสุดท้ายก็ต้องหา ห.ร.ม.
    แต่สามารถคิดได้ดังนี้ ก่อนอื่นเริ่มจากหาค่า sumOdd ,sumEven แล้วค่อยหา GCD ค่อย return
    พอมานั่งไล่ดูผลบวกแล้วก็ได้ค่า n พบความสั่มพันคือ odd = n x n, even = n x (n+1) เลยทำให้หาไวขึ่้น
    """
    def gcdOfOddEvenSums(self, n: int) -> int:

        # odd = 0
        # even = 0

        # for i in range(1,n*2,2):
        #     odd += i
        # for j in range(2,(n*2)+1,2):
        #     even += j

        odd = n * n
        even = n * (n+1)

        while odd != 0 :
            even ,odd = odd ,even % odd
        
        return even