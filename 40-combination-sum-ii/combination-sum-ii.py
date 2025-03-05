class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()  # Sort to handle duplicates

        def backtrack(start, combination, total):
            if total == target:
                result.append(list(combination))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                combination.append(candidates[i])
                backtrack(i + 1, combination, total + candidates[i])  # Move to the next index
                combination.pop()  # Backtrack

        backtrack(0, [], 0)
        return result
