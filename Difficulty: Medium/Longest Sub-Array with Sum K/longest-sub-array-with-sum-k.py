#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        x={}
        sum1=0
        max1=0
        for i in range(len(arr)):
            sum1+=arr[i]
            if sum1==k:
                max1=i+1
            if (sum1-k) in x:
                max1=max(max1,i-x[sum1-k])
            if sum1 not in x:
                x[sum1]=i
        return max1
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends