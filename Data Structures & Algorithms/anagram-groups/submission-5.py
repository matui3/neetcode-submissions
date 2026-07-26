class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            hashmap[sorted_word].append(word)
        
        for words in hashmap.keys():
            res.append(hashmap[words])
        
        return res