class Solution:
    def findTwoElement( self,arr): 
        n=len(arr)
        arr.sort()
        d=None
        s=sum(arr)
        for i in range(1,n):
            if arr[i]==arr[i-1]:
                d=arr[i]
                break
        sm=n*(n+1)//2
        m=sm-(s-d)
        return d,m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends