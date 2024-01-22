class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}
        for i in s:
            if i not in h1:
                h1[i] = 1
            else:
                h1[i] +=1

        for i in t:
            if i not in h2:
                h2[i] = 1
            else:
                h2[i] +=1
                
        if len(h1)!=len(h2):
            return False

        for i in h1:
            if i not in h2 or h2[i] != h1[i]:
                return False
        return True