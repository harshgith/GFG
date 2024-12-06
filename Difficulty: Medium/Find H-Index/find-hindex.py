class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        index = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                index = i + 1
            else:
                break
        return index

#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")

# } Driver Code Ends