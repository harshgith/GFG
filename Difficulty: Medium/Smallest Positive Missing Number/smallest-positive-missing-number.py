#User function Template for python3

class Solution:
    
    def missingNumber(self,arr):
        arr=[num for num in arr if num>0]
        num_set=set(arr)
        for i in range(1,len(arr)+2):
            if i not in num_set:
                return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends