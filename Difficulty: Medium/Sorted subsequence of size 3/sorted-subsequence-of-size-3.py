class Solution:
    def find3Numbers(self, arr):
        if len(arr) <= 2:
            return []
        
        # Initialize a list to store the smallest elements up to each index
        smalll = [float('inf') for _ in range(len(arr))]
        smalll[0] = arr[0]
        
        # Initialize a list to store the largest elements from each index to the end
        big = [float('-inf') for k in range(len(arr))]
        big[-1] = arr[-1]
        
        # Fill the smalll array with the minimum values up to each index
        for i in range(1, len(arr)):
            if smalll[i-1] <= arr[i]:
                smalll[i] = smalll[i-1]
            else:
                smalll[i] = arr[i]
        
        # Fill the big array with the maximum values from each index to the end
        for j in range(len(arr) - 2, -1, -1):
            if arr[j] >= big[j+1]:
                big[j] = arr[j]
            else:
                big[j] = big[j+1]
        
        # Check if there exists a triplet where smalll[ind] < arr[ind] < big[ind]
        for ind in range(len(arr)):
            if smalll[ind] < arr[ind] < big[ind]:
                return [smalll[ind], arr[ind], big[ind]]
        
        # Return an empty list if no such triplet is found
        return []



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def isSubSequence(v1, v2):
    m = len(v2)
    n = len(v1)
    j = 0  # For index of v2
    # Traverse v1 and v2
    for i in range(n):
        if j < m and v1[i] == v2[j]:
            j += 1
    return j == m


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        n = len(arr)
        obj = Solution()
        res = obj.find3Numbers(arr)
        if len(res) != 0 and len(res) != 3:
            print(-1)
        else:
            if not res:
                print(0)
            elif res[0] < res[1] < res[2] and isSubSequence(arr, res):
                print(1)
            else:
                print(-1)

# } Driver Code Ends