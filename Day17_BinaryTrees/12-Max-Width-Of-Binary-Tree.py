# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = []
        ans = -1
        q.append([root,0])
        while q:
            size = len(q)
            minPos = q[0][1]
            leftmost,rightmost = -1,-1
            for i in range(size):
                cur,pos = q.pop(0)
                pos -= minPos
                if i == 0:
                    leftmost = pos
                if  i == size -1:
                    rightmost = pos
                if cur.left:
                    q.append([cur.left,2*pos + 1])
                if cur.right:
                    q.append([cur.right,2*pos + 2])
            ans = max(ans,rightmost - leftmost + 1)
        return ans