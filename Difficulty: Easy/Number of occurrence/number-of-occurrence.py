from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def countFreq(self, arr: List[int], target: int) -> int:
        if not arr or target < arr[0] or arr[-1] < target:
            return 0
        start = bisect_left(arr, target)
        return bisect_right(arr[start:], target)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends