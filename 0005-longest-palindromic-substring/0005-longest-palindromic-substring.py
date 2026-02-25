class Solution:
    def longestPalindrome(self, s: str) -> str:
        return dp(s)


def dp(s: str) -> str:
    # top-down 2d dp, where tab[i][j] = true when s[i..j] is a palindrome
    # s[i..j] is a palindrome when tab[i+1][j-1] == true and s[i] == s[j]
    # this breaks when i..j is a short string of length <= 3 so we add the and condition to the check
    residx, reslen = 0, 0
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                dp[i][j] = True
                if reslen < (j - i + 1):
                    residx = i
                    reslen = j - i + 1
    
    return s[residx : residx + reslen]


def twopointer(s: str) -> str:
    if len(s) == 1:
        return s

    maxlen = 0
    maxpad = ''

    def expand(i: int) -> (int, str):
        padlen = 1
        padstr = s[i]
        if i == 0:
            return (padlen, padstr)
        a, b = i-1, i+1
        while a >= 0 and b < len(s) and s[a] == s[b]:
            padlen += 2
            padstr = s[a:b+1]
            a -= 1
            b += 1
        return (padlen, padstr)


    # odd
    for i in range(len(s)):
        curlen, curpad = expand(i)
        if curlen > maxlen:
            maxlen, maxpad = curlen, curpad

    # even
    curlen = 0
    for i in range(len(s)-1):
        a, b = i, i+1
        while a >= 0 and b < len(s) and s[a] == s[b]:
            curlen = b - a + 1
            if curlen > maxlen:
                maxlen = curlen
                maxpad = s[a:b+1]
            a -= 1
            b += 1
        curlen = 0
    
    return maxpad
