class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        h = {}
        h[0] = 1
        xor = 0
        for i in range (0,len(A)):
            xor^=A[i]
            
            k = xor ^ B
            if k in h:
                count +=h[k]    
            if xor not in h:
                h[xor] = 1
            else:
                h[xor] += 1
                

        return count 