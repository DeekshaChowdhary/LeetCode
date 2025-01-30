class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

# Example usage:
s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(s.longestCommonPrefix(["dog", "racecar", "car"]))   # Output: ""
