# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def SameTree(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            
            if not p or not q or p.val != q.val :
                return False

            return SameTree(p.left,q.left) and SameTree(p.right,q.right)
        

        return SameTree(p,q)
        