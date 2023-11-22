class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        s1 = strs[0]
        c= 0
        for i in s1:
            c1 = 0
            for j in strs[1:]:
                if i == j[c:c + 1]:
                    c1+=1
            if c1 == len(strs[1:]):
                ans+=i
            else:
                break
            c+=1
        return ans
