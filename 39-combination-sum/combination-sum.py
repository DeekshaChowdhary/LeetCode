class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, combination, total):
            if total == target:
                result.append(list(combination))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, combination, total + candidates[i])
                combination.pop()

        backtrack(0, [], 0)
        return result
