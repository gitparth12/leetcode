class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ''
        cur = ''
        for c in str2:
            cur += c
            if not len(str2) % len(cur) == 0 or not len(str1) % len(cur) == 0:
                continue
            if cur * int(len(str2)/len(cur)) == str2 and cur * int(len(str1)/len(cur)) == str1:
                res = cur
        return res