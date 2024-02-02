class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        # code here
        ans = []
        if root == None:
            return ans
        h = {}
        queue = []
        queue.append([root,0])
        while(queue):
            node,line = queue.pop(0)
            if line not in h:
                h[line] = node.data
            
            if node.left:
                queue.append([node.left,line - 1])
            if node.right:
                queue.append([node.right,line + 1])
            
            
        for i in sorted(h.keys()):
            ans.append(h[i])
        
        #print(h)
        return ans