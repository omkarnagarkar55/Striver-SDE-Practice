from typing import List

def stringMatch(text: str, pattern: str) -> List[int]:

    nl = len(pattern)
    hl = len(text)
    ans = []
    j = 0
    i = 0
    while i < hl:
        if text[i] == pattern[j]:
            j+=1
        else:
            i=i-j
            j = 0
        if j==nl:
            ans.append(i - (j-1)+1)
            i -=j-1
            j = 0
        i+=1
    return ans