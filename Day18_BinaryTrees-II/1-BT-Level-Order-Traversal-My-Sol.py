# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = []

        if root == None:
            return ans
        q.append(root)
        while q:
            size = len(q)
            levelNode = []
            for i in range(size):
                cur = q.pop(0)
                print(cur.val)
                levelNode.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.append(levelNode)
        return ans
                
        