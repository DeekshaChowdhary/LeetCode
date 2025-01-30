class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define the 32-bit integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Determine if the number is negative
        negative = x < 0

        # Work with the absolute value of x
        x = abs(x)

        # Reverse the digits
        reversed_x = 0
        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow before adding the digit
            if reversed_x > (INT_MAX - digit) // 10:
                return 0

            reversed_x = reversed_x * 10 + digit

        # Restore the sign
        if negative:
            reversed_x = -reversed_x

        # Ensure the reversed value is within the 32-bit signed integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0

        return reversed_x
