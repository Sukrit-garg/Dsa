# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        result=[]
        def helper(root,i):
        	if root==None:
        		return 
        	if len(result)<i+1:
        		result.append(root.val)
        	# else:
        	# 	result[i]=root.val
        	helper(root.right,i+1)
        	helper(root.left,i+1)
        helper(root,0)
        return result