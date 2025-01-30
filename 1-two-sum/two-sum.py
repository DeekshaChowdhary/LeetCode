class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the complement and its index
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            # Check if the complement exists in the dictionary
            if complement in num_map:
                return [num_map[complement], i]
            # Store the current number and its index in the dictionary
            num_map[num] = i
