# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(parent:TreeNode):
            if parent:
                inorder(parent.left)
                ans.append(parent.val)
                inorder(parent.right)
        inorder(root)
        return ans

        
        