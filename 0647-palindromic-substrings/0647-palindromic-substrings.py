class Solution(object):
    def countSubstrings(self, s):
        res = 0 

        for i in range(len(s)):
            res += self.countPali(s, i, i) # for odd length
            res += self.countPali(s, i, i+1) # for even length
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >=0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1 # expand on left side
            r += 1 # expand on right side
        return res