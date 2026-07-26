class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = defaultdict(list)

        for word in strs:
            groups[''.join(sorted(word))].append(word)

        for values in groups.values():
            res.append(values)

        return res