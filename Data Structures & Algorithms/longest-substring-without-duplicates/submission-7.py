class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        longest = 0
        l = 0

        for r in range(len(s)):
            if s[r] in char_map:
                l = max(l, char_map[s[r]] + 1)
            char_map[s[r]] = r
            longest = max(longest, r - l + 1)
        
        return longest
