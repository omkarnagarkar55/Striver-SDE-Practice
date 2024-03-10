# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hmap = {}
        for i in range(len(inorder)):
            hmap[inorder[i]] = i
        
        return self.buildTree1(0, len(postorder) - 1, postorder, 0, len(inorder) - 1, inorder, hmap)
    
    def buildTree1(self, poststart, postend, postorder, instart, inend, inorder, hmap):
        if poststart > postend or instart > inend:
            return None
        
        root = TreeNode(postorder[postend],None,None)

        inroot = hmap[root.val]
        numleft = inroot - instart
        numright = inend - inroot

        root.left =  self.buildTree1(poststart, poststart + numleft - 1, postorder, instart, instart + numleft, inorder, hmap)
        root.right = self.buildTree1(poststart + numleft, postend - 1, postorder, inroot + 1, inend, inorder, hmap)

        return root        
        