class Solution:
    def myPow(self, x: float, n: int) -> float:
        nn = n
        ans = 1.0
        if nn < 0:
            nn = -1 * nn
        while nn:
            print(ans)
            if nn % 2 == 0:
                x = x * x
                nn=nn//2
            else:
                ans = ans * x
                nn = nn - 1
        
        if n < 0:
            ans = 1.0 / ans
        return ans