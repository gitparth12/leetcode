class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) < len(s3): return False
        dp = defaultdict(lambda: False)  # dp[(i1, i2, i3)] = bool for if s1[i1:] and s2[i2:] can interleave s3[i3:]
        def dfs(i1, i2, i3):
            if i1 == len(s1) and i2 == len(s2) and i3 == len(s3):
                return True
            if i1 == len(s1):
                return s2[i2:] == s3[i3:]
            if i2 == len(s2):
                return s1[i1:] == s3[i3:]
            if i3 == len(s3):
                return False

            if (i1, i2, i3) in dp:
                return dp[(i1, i2, i3)]

            l1, l2, l3 = s1[i1], s2[i2], s3[i3]
            print(f'{i1}: {l1} | {i2}: {l2} | {i3}: {l3}')
            if l1 == l3:
                dp[(i1, i2, i3)] = dp[(i1, i2, i3)] or dfs(i1+1, i2, i3+1)
            if l2 == l3:
                dp[(i1, i2, i3)] = dp[(i1, i2, i3)] or dfs(i1, i2+1, i3+1)
            return dp[(i1, i2, i3)]

        return dfs(0, 0, 0)

        

# loop over s3: (keeping pointer in s1 and s2 with current letters l1, l2, l3)
#   at each point we have <= 2 choices
#   -   if l1 and l2 == l3: we either take l1, or take l2, but we recurse over both to get boolean out from the end of the branch
#   -   if only one of them is == l3, then we take that one and move on
# Because we alternate, even if we do multiple consecutive letters from s1 or s2, they can be considered one string so we end up with |n - m| <= 1