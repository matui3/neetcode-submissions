class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a hashmap
        hashset = {}
        # iterate over string
        for letter in s:
            # add each letter to the set
            hashset[letter] = 1 + hashset.get(letter, 0)
        
        for letter in t:
            if letter in hashset:
                hashset[letter] = hashset.get(letter) - 1
            else:
                return False
        
        for value in hashset.values():
            if value != 0:
                return False
        
        return True

        

        
