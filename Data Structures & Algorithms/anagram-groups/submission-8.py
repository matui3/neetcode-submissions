class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first create a dictionary with a list
        # then iterate through the word
        anagrams = defaultdict(list)
        res = []
        for word in strs:
            anagram = "".join(sorted(word))
            anagrams[anagram].append(word)
        
        for words in anagrams.values():
            res.append(words)

        return res