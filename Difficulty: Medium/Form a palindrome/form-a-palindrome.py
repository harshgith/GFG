class Solution:
    def LCM(self, S1, S2, n):
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif S1[i - 1] == S2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[n][n]
    def countMin(self, s):
        n = len(s)
        R_str = s[::-1]
        lcm = self.LCM(s, R_str, n)
        return n - lcm

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.countMin(Str))

# } Driver Code Ends