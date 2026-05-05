# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def soln(node: TreeNode):
            if not node:
                return 0
            
            left_depth = 1 + soln(node.left)
            right_depth = 1 + soln(node.right) 

            return max(right_depth,left_depth)
        
        return soln(root)
