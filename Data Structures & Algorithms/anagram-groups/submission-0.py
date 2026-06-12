class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       # trying naive solution first
       # sort each string ?
        sortedstrs = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            sortedstrs[sortedS].append(s)
        return list(sortedstrs.values())
        