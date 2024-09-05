#User function Template for python3
class Solution:
    def missingNumber(self, n, arr):
        # code here
        check=[i+1 for i in range(n)]
        sum_arr=sum(arr)
        sum_all=sum(check)
        return (sum_all - sum_arr)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(n, arr)
    print(s)

# } Driver Code Ends