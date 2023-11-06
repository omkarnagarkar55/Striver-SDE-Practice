class Solution:
    def reverseWords(self, s: str) -> str:
        a = list(filter(lambda a: a!='',list(map(lambda a: a.strip(),s.split(' ')))))
        return (" ".join(a[::-1]))