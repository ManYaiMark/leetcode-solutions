class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        # จริงๆใช้ self ได้ แต่ oop ค่อนข้างแย่
        def BTS(value):
            # เช็คว่า list หมดยัง
            if not value:
                return None
            # หาค่ากลาง เพื่อเป็น Node บนสุด
            h = len(value)
            m = h // 2
            # แบ่งซ้ายขวา
            left = value[0:m]
            right = value[m+1:h]
            # สร้าง Tree 
            root = TreeNode(value[m])
            # ใช้การ Recursion เพื่อทำการสร้าง Node ซ้ายขวา
            root.left = BTS(left)
            root.right = BTS(right)
            return root
        
        return BTS(nums)