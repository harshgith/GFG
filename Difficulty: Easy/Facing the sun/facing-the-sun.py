class Solution:
    def countBuildings(self, height):
        mel=height[0]
        c=1
        for i in range(1,len(height)):
            if mel<height[i]:
                c+=1
                mel=height[i]
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        height = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(height)
        print(ans)

# } Driver Code Ends