#User function Template for python3

class Solution:
    def minIncrements(self, arr): 
        arr.sort()
        ans = 0
        length = len(arr)
        
        for i in range(1 , length):
            if arr[i] == arr[i-1]:
                arr[i] += 1
                ans += 1
            
            elif arr[i] < arr[i-1]:
                ans += (arr[i-1]+1) - arr[i]
                arr[i] = arr[i-1]+1
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends