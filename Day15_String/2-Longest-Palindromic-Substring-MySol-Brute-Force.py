# BRUTE FORCE

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxlen = -1
        ans = ''
        # If the len of the string is 0 or 1 , then return the string
        if n == 1 or n == 0:
            return s
        else:
            # Generate every substring and check if it's a palindrome or not 
            for i in range(0,n):
                st = ''
                for j in range(i,n):
                    st+= s[j]
                    if st == st[::-1]:
                        # Only store the longest palindrome in the 'ans' variable
                        if maxlen < len(st):
                            maxlen = len(st)
                            ans = st
        return ans