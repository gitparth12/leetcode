class Solution:
    def countSubstrings(self, s: str) -> int:
        l, r = 0, 0
        count = 0
        for i in range(len(s)):
            # itself + odd-length palindromes + even-length palindromes
            count += 1 + expand(i-1, i+1, s) + expand(i, i+1, s)
        return count

def expand(l, r, s) -> int:
    # works for both odd and even length palindromes, we handle difference beforehand
    count = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        count += 1
        l, r = l-1, r+1
    return count

