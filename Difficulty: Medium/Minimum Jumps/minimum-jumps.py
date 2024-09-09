class Solution:
    def minJumps(self, arr):
        lth=len(arr)
        cur,prv,step=0,-1,0
        while cur<lth-1:
            mx=max([prv+1+ix+ve for ix,ve in enumerate(arr[prv+1:cur+1])])
            if mx>cur:
                cur,prv,step=mx,cur,step+1
            else:
                return -1
        return step


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)

# } Driver Code Ends