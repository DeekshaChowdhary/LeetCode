class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0  # Edge case: empty array

        i = 0  # Slow pointer

        for j in range(1, len(nums)):  # Fast pointer starts from index 1
            if nums[j] != nums[i]:  # If a new unique element is found
                i += 1  # Move the slow pointer
                nums[i] = nums[j]  # Place the unique element in the correct position

        return i + 1  # Return the count of unique elements
