class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # need a dictionary
        anagrams = defaultdict(list)
        # keep track of each word that is an anagram with each other
        string_groups = [] # need this to return all the anagrams together
        # need to iterate over the array
        for i in range(len(strs)):
            # we need to get a sorted word because if you sort this word and its the same as another word, it's anagram
            # we use the hashmap to keep track of whether we have encountered that sorted word before
            sorted_word = ''.join(sorted(strs[i]))
            if sorted_word in anagrams: # they key in this case is that if the sorted word is in the hashmap then append it to that list
                anagrams[sorted_word].append(strs[i])
            else:
                # if it's not, create a new list where the first item is strs[i]
                anagrams[sorted_word] = [strs[i]]
        
        # iterate through the values
        for words in anagrams.values():
            string_groups.append(words) # we add each list of words into the list

        return string_groups
