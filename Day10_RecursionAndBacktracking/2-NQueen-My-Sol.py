class Solution:
    #Checking if previous diagonals are occupied
    def isSafe(self,row ,col ,ds,n):
        row1 = row
        col1 = col
        while row >=0 and col >=0:
            row-=1
            col-=1
            if str(row) + str(col) in ds:
                return False
        
        while row1>=0 and col1<n:
            row1-=1
            col1+=1
            if str(row1) + str(col1) in ds:
                return False
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        a = []
        ds = []
        ans = []
        nums = [i for i in range(n)]
        def queenCheck(nums,row):
            if row == n:
                a.append(ds[:])
                return

            for i in range(len(nums)):
                if not self.isSafe(row,nums[i],ds,n):
                    continue
                ds.append(str(row)+str(nums[i]))
                queenCheck(nums[0:i] + nums[i+1:],row + 1)
                ds.pop()
        queenCheck(nums, 0)

        for i in a:
            r = []
            for j in i:
                val = ['.']*n
                val[int(j[1])] = 'Q'
                r.append("".join(val))
            ans.append(r)

        return ans