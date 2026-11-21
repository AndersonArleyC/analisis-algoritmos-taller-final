class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Return the minimum edits needed to transform word1 into word2."""
        rows = len(word1) + 1
        columns = len(word2) + 1
        dp = [[0] * columns for _ in range(rows)]

        for i in range(rows):
            dp[i][0] = i
        for j in range(columns):
            dp[0][j] = j

        for i in range(1, rows):
            for j in range(1, columns):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    delete = dp[i - 1][j]
                    insert = dp[i][j - 1]
                    replace = dp[i - 1][j - 1]
                    dp[i][j] = 1 + min(delete, insert, replace)

        return dp[-1][-1]
