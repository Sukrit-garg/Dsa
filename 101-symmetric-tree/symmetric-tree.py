# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left,right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            if left.val != right.val:
                return False
            comp_left = helper(left.left,right.right)
            if not comp_left:
                return False
            comp_right = helper(left.right,right.left)
            if not comp_right:
                return False
            return True
        return helper(root.left,root.right)
            