class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s

        self.start, self.max_length = 0, 0  # Use instance variables

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > self.max_length:
                    self.start, self.max_length = left, right - left + 1
                left -= 1
                right += 1

        for i in range(len(s)):
            expand_around_center(i, i)   # Odd-length palindrome
            expand_around_center(i, i+1) # Even-length palindrome

        return s[self.start:self.start + self.max_length]

# Example usage:
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(solution.longestPalindrome("cbbd"))   # Output:
