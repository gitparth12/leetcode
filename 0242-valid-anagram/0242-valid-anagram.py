class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anamap = {}  # hashmap of symbols and their frequency in string

        for c in s:
            try:
                anamap[c] += 1
            except KeyError:
                anamap[c] = 1

        for c in t:
            try:
                if anamap[c] > 0:
                    anamap[c] -= 1
                    if anamap[c] == 0:
                        anamap.pop(c)
                else:
                    return False
            except KeyError:
                return False

        if len(anamap) != 0:
            return False
        else:
            return True