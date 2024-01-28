# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        cur = root
        while cur:
            if cur.left == None:
                ans.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                # Go to the right most of the left
                while pre.right and pre.right!=cur:
                    pre = pre.right
                
                if pre.right == None:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    ans.append(cur.val)
                    cur = cur.right
        return ans

