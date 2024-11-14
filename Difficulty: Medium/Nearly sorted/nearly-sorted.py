#User function Template for python3
import heapq
class Solution:
    def nearlySorted(self, arr, k):
        heap = arr[:k + 1]
        heapq.heapify(heap)
        
        res = []
        i = 0
        curr = k + 1

        while curr < len(arr):
            poped = heapq.heappop(heap)
            arr[i] = poped
            
            heapq.heappush(heap, arr[curr])
            curr += 1
            i += 1
            
        while len(heap):
            curr = heapq.heappop(heap)
            arr[i] = curr
            i += 1
        
        return arr

#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        ob.nearlySorted(arr, k)
        print(*arr)
        # print("~")
        t -= 1
# } Driver Code Ends