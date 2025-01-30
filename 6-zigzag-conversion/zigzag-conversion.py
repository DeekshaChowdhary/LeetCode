class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Traverse the string
        for char in s:
            rows[current_row] += char
            # Change direction at the top or bottom of the zigzag
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        # Combine all rows
        return ''.join(rows)


# Example Usage
solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(solution.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(solution.convert("A", 1))              # Output: "A"
