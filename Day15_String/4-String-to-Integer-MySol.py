class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ''
        ll = -(2**31)
        ul = (2**31) - 1
        for i in s:
            if i == ' ':
                if ans == '':
                    continue
                else:
                    break
            if i == '-' or i == '+':
                if ans == '':
                    ans+=i
                else:
                    break
            elif 48 <= ord(i) <= 57:
                ans+=i
            else:
                break

        if ans not in ['','+','-']:
            ans = int(ans)
            if ll > ans:
                return ll
            elif ans > ul:
                return ul
            else:
                return ans
        else:
            return 0