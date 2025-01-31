from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Custom comparator function
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Convert all numbers to strings
        nums = list(map(str, nums))
        
        # Sort the numbers using the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join the sorted numbers into a single string
        result = ''.join(nums)
        
        # Handle the case where the result is "000...0"
        return '0' if result[0] == '0' else result
