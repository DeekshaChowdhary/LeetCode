class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i = 1  # Pointer to track the position to place the next valid element
        count = 1  # To count the frequency of the current element
        
        for j in range(1, len(nums)):
            if nums[j] == nums[j - 1]:
                count += 1
            else:
                count = 1  # Reset count for a new number
            
            if count <= 2:
                nums[i] = nums[j]  # Place the element in the valid position
                i += 1
        
        return i  # i represents the new length of the array with the required elements
