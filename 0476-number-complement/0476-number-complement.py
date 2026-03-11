class Solution:
    def findComplement(self, num: int) -> int:
        bin_str = bin(num)[2:]  # removed the '0b'
        res = []
        for i in range(len(bin_str)):
            res.append('0' if bin_str[i] == '1' else '1')
        return int(''.join(res), 2)
