class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Step 1: Sort the array
        res = []  # Store unique triplets
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1  # Two pointers
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate elements
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif total < 0:
                    left += 1  # Move left pointer to increase sum
                else:
                    right -= 1  # Move right pointer to decrease sum
        
        return res
