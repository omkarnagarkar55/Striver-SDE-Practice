class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        ans = []
        top  = -1
        stk = []
        
        for i in range(len(A)):
            if top == -1:
                ans.append(-1)
            elif stk[top] < A[i]:
                ans.append(stk[top])
            else:
                stk.pop()
                top -= 1
                while top >-1:
                    if stk[top] < A[i]:
                        ans.append(stk[top])
                        break
                    stk.pop()
                    top -= 1
                if top == -1:
                    ans.append(-1)
            stk.append(A[i])
            top+=1
        return ans
