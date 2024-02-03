from os import *
from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    # Write your code here.
    ans = []
    inord = []
    preord = []
    posord = []

    def traversal(root):
        if root == None:
            return
        
        preord.append(root.data)
        traversal(root.left)
        inord.append(root.data)
        traversal(root.right)
        posord.append(root.data)
    
    traversal(root)
    return [inord,preord,posord]
