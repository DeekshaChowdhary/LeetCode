class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # Stack stores indices, starting with -1 to handle edge cases
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push index of '('
            else:
                stack.pop()  # Pop last '(' index
                if stack:
                    max_length = max(max_length, i - stack[-1])  # Update max length
                else:
                    stack.append(i)  # Push current index as new base
        
        return max_length
