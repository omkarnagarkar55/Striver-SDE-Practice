# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[]
        ans = []
        level = 0
        if root == None:
            return ans
        q.append(root)

        while q:
            size = len(q)
            nodeList = []
            for i in range(size):
                cur = q.pop(0)
                nodeList.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if level % 2 != 0:
                ans.append(nodeList[::-1])
            else:
                ans.append(nodeList)
            level +=1

        return ans
        