class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        s1_counter = Counter(s1) # dictionary like object that counts the freq of the letters
        window_counter = Counter(s2[:n]) # another object like that - basically you're gonna shift this

        if s1_counter == window_counter:
            return True
        
        # fixed window
        for i in range(n, m):

            window_counter[s2[i]] += 1
            window_counter[s2[i - n]] -= 1

            if s1_counter == window_counter:
                return True
        

        return False