class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def solve(s1,s2):
            m=len(s1)
            n=len(s2)
            dp=[[0 for i in range(n+1)]for j in range(m+1)]
            for i in range(m+1):
                dp[i][0]=i
            for j in range(n+1):
                dp[0][j]=j 
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if s1[i-1]==s2[j-1]:
                        dp[i][j]=dp[i-1][j-1]
                    else:
                        dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
            return dp[m][n]
        return solve(word1,word2)