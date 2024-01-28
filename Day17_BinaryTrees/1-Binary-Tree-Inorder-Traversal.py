# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def inorder(cur):
            if cur == None:
                return
            
            inorder(cur.left)
            ans.append(cur.val)
            inorder(cur.right)
        
        inorder(root)
        return ans