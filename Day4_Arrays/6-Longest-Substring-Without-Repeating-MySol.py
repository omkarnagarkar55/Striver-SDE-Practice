class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = -1
        l=[]
        c=0
        for i in s:
            if i not in l:
                l.append(i)    # Store in the list if the element is not present in the list
            else:
                c = len(l)
                l=l[l.index(i)+1:] # Only take all the elements right of the repeated element
                l.append(i)
            if c > maxCount:
                maxCount = c

        if len(l) > maxCount:
            maxCount = len(l)
        
        return maxCount
            


        