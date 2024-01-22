from typing import List

def stringMatch(text: str, pattern: str) -> List[int]:
    # Calculate the lengths of the 'text' and 'pattern' strings.
    n = len(text)
    m = len(pattern)

    # List storing the indices of occurrences.
    ans = []

    # Initializing LPS (Longest Proper Prefix which is also Suffix) array.
    lps = [0] * m
    i = 1
    j = 0
    while i < m:
        if pattern[i] == pattern[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            # If there is a mismatch, move the j pointer based on lps array.
            j = lps[j - 1]
        else:
            lps[i] = 0
            i += 1

    i = 0
    j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        elif j > 0:
            # If there is a mismatch, move the j pointer based on lps array.
            j = lps[j - 1]
        else:
            i += 1

        # If the entire pattern is found, add the starting index to the answer list.
        if j == m:
            ans.append(i - m+1)
            j = lps[j - 1]

    return ans