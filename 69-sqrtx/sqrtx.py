class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x  # If x is 0 or 1, the square root is x itself
        
        left, right = 0, x  # Set the range for binary search
        while left <= right:
            mid = (left + right) // 2  # Find the middle point
            mid_squared = mid * mid
            
            if mid_squared == x:
                return mid  # Found the exact square root
            elif mid_squared < x:
                left = mid + 1  # We need to search the right half
            else:
                right = mid - 1  # We need to search the left half
        
        return right  # After the loop, right is the floor of the square root
