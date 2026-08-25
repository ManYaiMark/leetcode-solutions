# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        root_left = root.left
        root_right = root.right

        def SameTree(p: TreeNode, q: TreeNode) -> bool:
            
            if not p and not q:
                return True
            
            if not p or not q or p.val != q.val :
                return False

            return SameTree(p.left,q.right) and SameTree(p.right,q.left)
        

        return SameTree(root_left,root_right)
