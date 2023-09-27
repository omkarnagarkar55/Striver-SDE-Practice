    def maxLen(self, n, arr):
        #Code here
        sumArr = {}
        ans = 0
        s = 0
        for i in range(len(arr)):
            s = s + arr[i] 
            if i not in sumArr:
                sumArr[s] = i
            else:
                ans = max(ans,i - sumArr[s])
        return ans		