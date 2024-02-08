# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = {}  # {vertical: {level: [nodes]}}
        todo = [(root, (0, 0))]  # Queue for BFS: [(node, (vertical, level))]
        
        while todo:
            temp, (x, y) = todo.pop(0)  # Current node and its position
            
            if x not in nodes:
                nodes[x] = {}
            if y not in nodes[x]:
                nodes[x][y] = []
            nodes[x][y].append(temp.val)
            
            if temp.left:
                todo.append((temp.left, (x-1, y+1)))
            if temp.right:
                todo.append((temp.right, (x+1, y+1)))
        
        ans = []
        for x in sorted(nodes):  # Sort by vertical
            col = []
            for y in sorted(nodes[x]):  # Sort by level
                col.extend(sorted(nodes[x][y]))  # Sort nodes at the same level
            ans.append(col)
        
        return ans