class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = {}
        left = 0
        max_len = 0 

        for right in range(len(s)):
            if s[right] in found and found[s[right]] >= left:
                left = found[s[right]] + 1
            found[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len


