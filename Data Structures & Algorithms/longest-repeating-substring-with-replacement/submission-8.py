class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        count_repeating_dict = {}
        repeat_chars_count = 0

        for r in range(len(s)):
            count_repeating_dict[s[r]] = 1 + count_repeating_dict.get(s[r], 0)
            repeat_chars_count = max(count_repeating_dict[s[r]], repeat_chars_count)
            
            while ((r - l + 1) - repeat_chars_count > k):
                count_repeating_dict[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest

