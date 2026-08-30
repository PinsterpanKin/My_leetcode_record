class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(start, path, target):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                backtrack(i, path + [candidates[i]], target - candidates[i])
        
        backtrack(0, [], target)
        return res