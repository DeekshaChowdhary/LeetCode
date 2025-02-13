class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2  # Find the middle index

            if nums[mid] == target:
                return mid  # Target found at mid

            # Determine which side is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:  # Target is in the left sorted half
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:  # Target is in the right sorted half
                    left = mid + 1
                else:
                    right = mid - 1

        return -1  # Target not found
