class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_replace_freq = {}
        max_repeat_char_count = 0

        l = 0
        longest = 0

        for r in range(len(s)):

            char_replace_freq[s[r]] = 1 + char_replace_freq.get(s[r], 0)
            max_repeat_char_count = max(max_repeat_char_count, char_replace_freq[s[r]])

            while ((r - l + 1) - max_repeat_char_count > k):
                char_replace_freq[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest



