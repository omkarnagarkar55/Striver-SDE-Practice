class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged=[]
        intervals.sort()
        for item in intervals:
            if len(merged)== 0 :
                merged.append(item)
            elif merged[-1][1] < item[0]:
                merged.append(item)
            else:
                merged[-1][1]=max(merged[-1][1],item[1])
        return merged
