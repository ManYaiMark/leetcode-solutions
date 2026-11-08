class Solution:    
    """
    โจทย์: กำหนดตาราง 2 มิติ grid และจำนวนเต็ม k ให้เลื่อนสมาชิกทุกตัวไปทางขวาจำนวน k ครั้ง 
    โดยเมื่อสมาชิกถึงท้ายแถวให้ย้ายไปต้นแถวถัดไป และเมื่อถึงท้ายตารางให้วนกลับไปตำแหน่งแรก จากนั้นคืนค่าตารางหลังจากเลื่อนเสร็จ

    วิธีคิด
    เปลี่ยน 2d -> 1d -> shif -> 2d
    ข้อนี้ค่อนข้างยากเพราะไม่เคยทำแนวนี้เลยนาน + ประสิทธิภาพต่ำ
    """
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        p = m*n
        if p == k :
            return grid
        def flatten_generator(two_d_list):
            for row in two_d_list:
                for item in row:
                    yield item
        # ต้องไปเรียนการใช้ yield เพิ่ม เพราะยังไม่เข้าใจลึกพอ
        grid = list(flatten_generator(grid))       
        # สามารใช้
        # for row in grid :
        #     l.extend(row)
        #     ใช้ extend เพื่อให้ง่ายต่อการอ่าน เขียนขึ้น

        # หาค่าที่ต้องเลื่อน โดยการหาเศษ
        k = k % (p)
        # เลื่อนโดยใช้เศษ หรือก็คือ shif
        l = grid[(p)-k:p] + grid[0:(p)-k]

        # ทำให้เป็น 2d
        def chunk_generator(one_d_list, size):
            it = iter(one_d_list)
            while item := list(islice(it, size)):
                yield item

        # สามารถใช้อแบบนี้้้เพื่อง่ายต่อการเขียน
        # result
        # for i in range(0, p, n):
        #     result.append(l[i:i+n])

        return list(chunk_generator(l,n))
