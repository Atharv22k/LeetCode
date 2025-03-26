class Solution:
    def isMatch(self, s: str, p: str) -> bool:
         # Lengths of the string and pattern
        m, n = len(s), len(p)
        
        # Create a DP table with (m + 1) x (n + 1)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty pattern can match with empty string
        dp[0][0] = True
        
        # Fill the first row for patterns with '*' that can match with an empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' can represent no characters (dp[i][j-1]) or one more character (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # Characters match or '?' wildcard
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]