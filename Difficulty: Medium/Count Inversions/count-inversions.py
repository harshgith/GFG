class Solution:
    def inversionCount(self, arr):
        self.count = 0  
        
        def merge_sort(arr, temp, left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort(arr, temp, left, mid)
                merge_sort(arr, temp, mid + 1, right)
                merge(arr, temp, left, mid, right)
        def merge(arr, temp, left, mid, right):
            i = left      
            j = mid + 1   
            k = left      
            inv_count = 0
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    inv_count += (mid - i + 1)  
                    j += 1
                k += 1
            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1
            while j <= right:
                temp[k] = arr[j]
                j += 1
                k += 1
            for i in range(left, right + 1):
                arr[i] = temp[i]
            self.count += inv_count
        n = len(arr)
        temp = [0] * n
        merge_sort(arr, temp, 0, n - 1)
        return self.count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends