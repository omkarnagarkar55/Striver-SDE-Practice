'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    cur = root
    ans = []
    
    def leftv(cur,level):
        if cur == None:
            return
        if level == len(ans):
            ans.append(cur.data)
        
        leftv(cur.left,level + 1)
        leftv(cur.right,level + 1)
    
    leftv(cur,0)
    return ans