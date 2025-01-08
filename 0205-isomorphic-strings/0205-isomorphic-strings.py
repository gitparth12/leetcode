class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Hashmap that tracks the mapped characters from one string to another
        sMap = {}
        tMap = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if not sMap.get(s[i]):
                sMap[s[i]] = t[i]
            if not tMap.get(t[i]):
                tMap[t[i]] = s[i]
            if sMap[s[i]] != t[i] or tMap[t[i]] != s[i]:
                return False
        return True