class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nl = len(needle)
        hl = len(haystack)

        j = 0
        i = 0
        while i < hl:
            if haystack[i] == needle[j]:
                j+=1
            else:
                i=i-j
                j = 0
            if j==nl:
                return i - (j-1)
            i+=1
        return -1