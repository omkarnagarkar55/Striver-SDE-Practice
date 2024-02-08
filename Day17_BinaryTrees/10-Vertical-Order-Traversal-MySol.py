# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        h = {}
        def traversal(root,col,level):
            if root == None:
                return
            
            if col not in h:
                h[col] = [[level,root.val]]
            else:
                h[col].append([level,root.val])

            traversal(root.left, col - 1 , level + 1)
            traversal(root.right, col + 1 , level + 1)
        traversal(root,0,0)
        hKey = list(h.keys())
        hKey.sort()
        for i in hKey:
            h[i].sort(key = lambda x:(x[0],x[1]))
            l = []
            for j in h[i]:
                l.append(j[1])
            ans.append(l)

        return ans