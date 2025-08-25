class Solution:
    # Stack approach
    def decodeString(self, s: str) -> str:
        stack = []
        num_cur = 0
        str_cur = ""

        # if c is digit -> add to current num
        # if c is [ -> push num, str to stack
        # if c char -> add to current str
        # if c is ] -> pop num, prev from stack; append prev + num * current str
        for c in s:
            if c.isdigit():
                num_cur = num_cur * 10 + int(c)
            elif c == '[':
                stack.append((num_cur, str_cur))
                num_cur = 0
                str_cur = ''
            elif c == ']':
                num, prev = stack.pop()
                str_cur = prev + str_cur * num
            else:
                str_cur += c
        return str_cur