#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        arr=[]
        for i in range(len(b)):
            arr.append(b[i])
        for i in range(len(a)):
            arr.append(a[i])
        arr.sort()
        return arr[k-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends