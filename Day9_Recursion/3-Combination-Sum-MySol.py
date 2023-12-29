class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        ds = []
        n = len(candidates)
        def subcombi(target):
            if target == 0:
                ds.sort()
                ans.add(tuple(ds[:]))
                return

            for i in range(n):
                if candidates[i] <= target:
                    ds.append(candidates[i])
                    subcombi(target - candidates[i])
                    ds.remove(candidates[i])

        subcombi(target)

        return [list(item) for item in ans]