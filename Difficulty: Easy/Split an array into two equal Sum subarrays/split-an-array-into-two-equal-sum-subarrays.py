class Solution:
    def canSplit(self, arr):

        totals=sum(arr)
        if totals%2!=0:
            return False
        target=totals//2
        curr=0
        for num in arr:
            curr +=num
            if curr==target:
                return True
        return False

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends