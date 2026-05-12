# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_num(self,root,num):
        if not root:
            return False
        res = False
        if num>root.val:
            res = self.find_num(root.right,num)
        elif num<root.val:
            res = self.find_num(root.left,num)
        else:
            return True
        return res
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root or (not root.left and not root.right):
            return False
        def helper(node):
            required = k - node.val
            if required!= node.val and self.find_num(root,required):
                return True
            check_left,check_right = False,False
            if node.left:
                check_left = helper(node.left)
            if node.right:
                check_right = helper(node.right)
            if check_left or check_right:
                return True
            return False
        return helper(root)
