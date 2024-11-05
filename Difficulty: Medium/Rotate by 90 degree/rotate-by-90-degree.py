#User function Template for python3

def rotate(mat): 
    n = len(mat)
    for i in range(n//2):
        for j in range(i,n-(i+1)):
            a = mat[i][j]
            b = mat[j][n-1-i]
            c = mat[n-1-i][n-1-j]
            d = mat[n-1-j][i]
            
            mat[i][j] = d
            mat[j][n-1-i] = a
            mat[n-1-i][n-1-j] = b
            mat[n-1-j][i] = c
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        matrix = []
        for i in range(N):
            arr = [int(x) for x in input().strip().split()]
            matrix.append(arr)

        rotate(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end=' ')
            print()
        print("~")

# } Driver Code Ends