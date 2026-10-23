class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        '''
        # โจทย์กำหนดค่าจะต่ำสุดคือ 1 และมากสุดคือ 100 เลยดักไว้
        # min_c ,max_c = 101,-1
        # หาค่าที่เล็กที่สุดและใหญ่ที่สุด
        for num in nums:
            if num < min_c :
                min_c = num
            if num > max_c :
                max_c = num
        n = []
        # ลูปเพื่อหา เริ่มจาก min + 1 เพราะจะได้ไวขึ้นละตัวสุด้ทายคือ n-1 
        for i in range(min_c+1,max_c):
            if i not in nums:
                n.append(i)
        '''
        # ใช้ set ในการเก็บค่าแทน list เพราะไวกว่า
        nums = set(nums)
        # หาโดยใช้ function เพราะความเร็วไม่ต่างกับการเขียนเอง
        min_c ,max_c = min(nums),max(nums)
        # ใช้ List comprehension ในการย่อ เพราะความเร็วความเร็วเยอะกว่าการประกาศ n = []
        return [i for i in range(min_c+1,max_c) if i not in nums]