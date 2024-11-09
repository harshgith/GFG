class Solution:
    def minSum(self, arr):
        arr.sort()
        num1 = ''
        num2 = ''
        for i in range(len(arr)):
            if i % 2 == 0:
                num1 += str(arr[i])
            else:
                num2 += str(arr[i])
        def addStrings(num1, num2):
            i, j = len(num1) - 1, len(num2) - 1
            carry = 0
            result = []
            
            while i >= 0 or j >= 0 or carry:
                n1 = int(num1[i]) if i >= 0 else 0
                n2 = int(num2[j]) if j >= 0 else 0
                total = n1 + n2 + carry
                carry = total // 10
                result.append(str(total % 10))
                i -= 1
                j -= 1
            return ''.join(result[::-1])
        sum_str = addStrings(num1, num2)
        sum_str = sum_str.lstrip('0')
        return sum_str if sum_str else '0'

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends