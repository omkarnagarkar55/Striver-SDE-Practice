class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nl = len(needle)
        hl = len(haystack)

        for i in range(hl-nl+1):
            if haystack[i:i+nl] == needle:
                return i
        return -1