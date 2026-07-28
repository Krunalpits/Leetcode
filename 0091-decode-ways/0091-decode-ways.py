class Solution:
    def numDecodings(self, s):
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1                              # base case: empty string = 1 way

        for i in range(n - 1, -1, -1):         # go backwards
            if s[i] == "0":
                dp[i] = 0                      # "0" can't be decoded
            else:
                dp[i] = dp[i + 1]              # take 1 digit

                if i + 1 < n and int(s[i:i+2]) <= 26:  # take 2 digits if valid
                    dp[i] += dp[i + 2]

        return dp[0]