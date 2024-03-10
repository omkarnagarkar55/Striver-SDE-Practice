# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hmap = {}
        for i in range(len(inorder)):
            hmap[inorder[i]] = i
        
        return self.buildTree1(0, len(preorder) - 1, preorder, 0, len(inorder) - 1, inorder, hmap)
        
    def buildTree1(self, prestart, preend, preorder, instart, inend, inorder, hmap):
        if prestart > preend or instart > inend:
            return None
        
        root = TreeNode(preorder[prestart],None,None)

        inroot = hmap[root.val]
        numleft = inroot - instart

        root.left =  self.buildTree1(prestart + 1, prestart + numleft, preorder, instart, instart + numleft, inorder, hmap)
        root.right = self.buildTree1(prestart + numleft + 1, preend, preorder, inroot + 1, inend, inorder, hmap)

        return root