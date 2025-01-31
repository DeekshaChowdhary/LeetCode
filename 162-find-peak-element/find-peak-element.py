class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid  # Peak is on the left (including mid)
            else:
                low = mid + 1  # Peak is on the right (excluding mid)
        return low  # At the end, low == high, pointing to a peak
