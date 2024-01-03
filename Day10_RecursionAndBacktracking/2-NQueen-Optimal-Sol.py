class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        a = []
        ds = []
        ans = []
        nums = [i for i in range(n)]
        # Hashtable
        upperDiagonal = [0]*(2*n - 1)
        lowerDiagonal = [0]*(2*n - 1)
        def queenCheck(nums,row):
            if row == n:
                a.append(ds[:])
                return

            for i in range(len(nums)):
                if upperDiagonal[n-1 + row - nums[i]] == 0 and lowerDiagonal[row + nums[i]] == 0:
                    ds.append(str(row)+str(nums[i]))
                    upperDiagonal[n-1 + row - nums[i]] = 1
                    lowerDiagonal[row + nums[i]] = 1
                    
                    queenCheck(nums[0:i] + nums[i+1:],row + 1)
                    
                    ds.pop()
                    upperDiagonal[n-1 + row - nums[i]] = 0
                    lowerDiagonal[row + nums[i]] = 0
        queenCheck(nums, 0)

        for i in a:
            r = []
            for j in i:
                val = ['.']*n
                val[int(j[1])] = 'Q'
                r.append("".join(val))
            ans.append(r)

        return ans