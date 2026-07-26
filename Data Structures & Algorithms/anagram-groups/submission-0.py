class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create result list
        # iterate through the list
        # take each word and sort it
        # create a hashmap with a sorted word and a list of the original words
        res = []
        hashmap = {}

        for word in strs:
            sorted_word = ''.join(sorted(word)) # sort each word
            if sorted_word in hashmap: # if the word is in the hashmap append it to the current list
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = [word] # if it's not create a list with that word
        
        for anagrams in hashmap.values(): # iterate through the values and append it to the resulting array
            res.append(anagrams)
        
        return res

            
