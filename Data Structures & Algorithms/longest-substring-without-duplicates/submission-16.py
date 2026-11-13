class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #abcb
        window = set()
        left, max_len = 0, 0 

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len