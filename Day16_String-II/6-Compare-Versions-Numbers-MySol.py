class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        v1, v2 = list(map(int, version1.split('.'))), list(map(int, version2.split('.')))
        
        n = len(v1)
        m = len(v2)

        if n > m:
            v2 = v2 + [0]*(n-m)
        elif n < m:
            v1 = v1 + [0]*(m-n)
        
        for i in range(len(v1)):
            if v1[i] == v2[i]:
                continue
            
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0