class Solution:
    def maximumMeetings(self,n,start,end):
        arr=[]
        for i in range(n):
            arr.append([start[i], end[i]])
        arr.sort(key=lambda x:x[1])
        i=0
        ans=1
        i=0
        for j in range(1,n):
            if arr[j][0]>arr[i][1]:
                ans+=1
                i=j
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends