class Solution:
    def countAndSay(self, n: int) -> str:
        h = {}
        ans = ''
        for i in range(n):
            a = ''
            if i == 0:
                ans+= "1"
                continue
            for j in range(len(ans)):
                if ans[j] in h:
                    h[ans[j]]+=1
                else:
                    h[ans[j]] = 1
                if j!=len(ans)-1:
                    if ans[j]!=ans[j+1] and ans[j] in h:
                            a+= str(h[ans[j]]) + ans[j]
                            h[ans[j]] = 0
                            
                elif ans[j] in h:
                    a+= str(h[ans[j]]) + ans[j]
                    h[ans[j]] = 0
            if a:
                ans = a
        return ans