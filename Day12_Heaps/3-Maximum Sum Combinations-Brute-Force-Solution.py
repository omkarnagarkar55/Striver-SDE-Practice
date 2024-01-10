class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        msum = []

        for i in A:
            for j in B:
                msum.append((i + j))
        
        msum.sort(reverse = True)
        return msum[0:C]