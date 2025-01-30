class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Convert the number to a string and compare with its reverse
        str_x = str(x)
        return str_x == str_x[::-1]

# Example usage
solution = Solution()
print(solution.isPalindrome(121))   # Output: True
print(solution.isPalindrome(-121))  # Output: False
print(solution.isPalindrome(10))    # Output: False
