class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # brute force
        # iterate through string 2. and create a window that is the same len as str1
        # sort each substring and str1, if its the same then return true
        # if s2 is not as long as s1 then there's no permutation of s1
        if len(s2) < len(s1):
            return False
        
        # permutation
        permutation = ''.join(sorted(s1))
        window_size = len(s1)
        l = 0
        for r in range(window_size -1, len(s2)):
            sorted_substring = ''.join(sorted(s2[l:r+1]))
            if permutation == sorted_substring:
                return True
            else:
                l += 1

        return False
            
        