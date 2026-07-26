class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        n, m = len(s1), len(s2)
        if n > m: 
            return False

        s1_count = Counter(s1)

        window_count = Counter(s2[:n])

        if s1_count == window_count:
            return True

        for i in range(n, m):
            window_count[s2[i]] += 1

            window_count[s2[i - n]] -= 1

            if s1_count == window_count:
                return True

        return False

