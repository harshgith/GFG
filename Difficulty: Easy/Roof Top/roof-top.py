class Solution:
    def maxStep(self, arr):
        m1=0
        c1=0
        
        for index in range(1, len(arr)):
            if arr[index-1]<arr[index]:
                c1+=1
            else:
                c1=0
            m1=max(m1, c1)
        
        
        return m1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends