class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_length = 0
        left = 0  # Left pointer of the window

        for right in range(len(s)):
            # Update the frequency of the current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Calculate the maximum frequency of any character in the current window
            max_freq = max(freq.values())

            # If the number of replacements needed exceeds k, shrink the window
            # characters needed to be replaced:
            replacements = (right - left + 1) - max_freq 
            if replacements > k:
                freq[s[left]] -= 1  # Decrease the frequency of the character at the left pointer
                left += 1  # Move the left pointer to the right

            # Update the maximum length of the window
            max_length = max(max_length, right - left + 1)

        return max_length