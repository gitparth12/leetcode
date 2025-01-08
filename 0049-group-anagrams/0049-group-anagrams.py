class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sMap = {}
        for s in strs:
            current = ''.join(sorted(s))
            if sMap.get(current) is None:
                sMap[current] = [s]
            else:
                sMap[current].append(s)
        return sMap.values()