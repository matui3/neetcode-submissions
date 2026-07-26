class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = defaultdict(list)

        for word in strs:
            groupMap[''.join(sorted(word))].append(word)
        
        return list(groupMap.values())
        
