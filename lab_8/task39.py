class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        def dfs(start_idx, current_sum, current_set):
            if current_sum == target:
                result.append(list(current_set))
                return
            if current_sum > target:
                return
            for i in range(start_idx, len(candidates)):
                current_set.append(candidates[i])
                dfs(i, current_sum + candidates[i], current_set)
                current_set.pop()
        dfs(0, 0, [])
        return result