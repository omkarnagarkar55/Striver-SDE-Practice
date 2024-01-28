def getPreOrderTraversal(root):
    # Write your code here.
	ans = []
	cur = root
	while cur:
		if cur.left == None:
			ans.append(cur.data)
			cur = cur.right
		else:
			pre = cur.left
			# Go to the right most of the left
			while pre.right and pre.right!=cur:
				pre = pre.right
			
			if pre.right == None:
				pre.right = cur
				ans.append(cur.data)
				cur = cur.left
			else:
				pre.right = None
				cur = cur.right
	return ans