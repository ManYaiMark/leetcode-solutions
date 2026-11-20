# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    โจทย์: กำหนด Binary Tree root ให้ตรวจสอบว่าต้นไม้เป็น height-balanced หรือไม่ 
    โดยสำหรับทุก Node ความสูงของ subtree ฝั่งซ้ายและฝั่งขวาต้องแตกต่างกันไม่เกิน 1 หากเป็นให้คืน true ไม่เช่นนั้นคืน false

    วิธีคิด
    หาว่ามัน HL - HR > 1 ไหม ถ้าใช่ก็ -1 จากนั้นระบบก็จะ return -1 จนกว่าจะจบ recursion(ฟังชั่นแบบ loop)
    ข้อนี้ทำผมปวดหัวมาก เพราะเป็นข้อที่ใช้ recursion เป้นจุดอ่อนเลย เลยทำให้ข้อนี้ทำนานหน่อย แต่ก็เค้นทำจนเสร้จ
    """
    def isBalanced(self, root: TreeNode | None) -> bool:
        def height(node):
            if node == None :
                return 0
            Hleft = height(node.left)
            if Hleft == -1:
                return -1
            Hright = height(node.right)
            if Hright == -1:
                return -1
            if abs(Hleft - Hright) > 1:
                return -1
            return 1 + max(Hleft , Hright)
        h = height(root)
        if h == -1 :
            return False
        
        return True
