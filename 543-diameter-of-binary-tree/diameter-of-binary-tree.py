# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dist = 0
        def helper(root):
            nonlocal max_dist
            if not root:
                return 0
            left_d = helper(root.left)
            right_d = helper(root.right)
            max_dist = max(max_dist, left_d + right_d)
            return max(left_d,right_d)+1
        helper(root)
        return max_dist