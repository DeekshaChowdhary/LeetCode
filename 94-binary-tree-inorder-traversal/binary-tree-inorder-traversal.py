# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def traverse(node):
            if not node:
                return []
            # Recursive inorder traversal: left -> root -> right
            return traverse(node.left) + [node.val] + traverse(node.right)
        
        return traverse(root)
