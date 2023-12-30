class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        n = len(candidates)
        candidates.sort()
        def subcombi(ind,target):
            if target == 0:
                ans.append(ds[:])
            for i in range(ind,n):
                if i!=ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i] <= target:
                    ds.append(candidates[i])
                    subcombi(i+1,target - candidates[i])
                    ds.pop()

        subcombi(0,target)

        return ans