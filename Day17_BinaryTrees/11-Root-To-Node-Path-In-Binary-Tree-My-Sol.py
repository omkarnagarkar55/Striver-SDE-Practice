'''
    Following is the class structure of the BinaryTreeNode class:

    class BinaryTreeNode:
        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None

'''
from typing import List

def allRootToLeaf(root) -> List[str]:
    # Write your code here.
    ans = []
    ds = []
    if root == None:
        return []
    
    ds.append(str(root.data))
    def pathL(root):
        if root.left == None and root.right == None:
            ans.append(' '.join(ds[:]))
            return
        if root == None:
            return
        if root.left:
            ds.append(str(root.left.data))
            pathL(root.left)
            ds.pop()
        if root.right:
            ds.append(str(root.right.data))
            pathL(root.right)
            ds.pop()
    
    pathL(root)

    return ans