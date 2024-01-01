class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        ds = []
        n = len(s)

        def subCombi(ind):
            if ind == n:
                ans.append(ds[:])
                return
            for i in range(ind,n):
                if self.isPalindrom(s[ind:i+1]):
                    ds.append(s[ind:i+1])
                    subCombi(i+1)
                    ds.pop()

        subCombi(0)
        return ans 
        

    def isPalindrom(self,s):
        if s == s[::-1]:
            return True
        else:
            return False