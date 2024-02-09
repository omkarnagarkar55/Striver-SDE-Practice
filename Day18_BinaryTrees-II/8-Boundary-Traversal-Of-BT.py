'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Binary Tree.
'''

# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# Functions to traverse on each part.
def traverseBoundary(root):
    # Write your code here.
    leftview = []
    rightview = []
    bottomview = []

    # Left Traversal 
    def traverseLeft(root):
        leftview.append(root.data)
        cur = root.left

        while(cur):
            if cur.left !=None or cur.right!=None:
                leftview.append(cur.data)
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right

    # Leaf nodes of the tree
    def boundary(root,level,col):
        if root == None:
            return

        if root.left == None and root.right == None:
            bottomview.append(root.data)
            
        boundary(root.left,level + 1,col - 1)
        boundary(root.right,level + 1,col + 1)
    
    # Right part of the tree
    def traverseRight(root):
        cur = root.right
        while(cur):
            if cur.left !=None or cur.right!=None:
                rightview.append(cur.data)
            if cur.right:
                cur = cur.right
            else:
                cur = cur.left

    boundary(root,0,0)
    traverseRight(root)
    traverseLeft(root)
    ans = leftview + bottomview + rightview[::-1]
    return ans