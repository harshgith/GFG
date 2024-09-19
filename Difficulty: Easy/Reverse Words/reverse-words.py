class Solution:
    def reverseWords(self,str):
        l = str.split(".")
        l = l[::-1]
        s = ""
        for i in l:
            s += i+"."
        s = s[:len(s)-1]
        return s


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends