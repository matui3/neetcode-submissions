class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_characters_repeated = 0
        char_freq = {}
        l = 0
        for r in range(len(s)):
            char_freq[s[r]] = 1 + char_freq.get(s[r], 0)

            max_characters_repeated = max(char_freq[s[r]], max_characters_repeated)


            while ((r - l + 1) - max_characters_repeated > k):
                char_freq[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, (r - l + 1))

        return max_length