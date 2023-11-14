#User function Template for python3

def findElement( arr, n):
    pre = [0 for x in range(n)]
    post = [float("inf") for y in range(n)]
    next = arr[0]
    for i in range(n):
        pre[i] = max(next, arr[i])
        next = pre[i]
    
    prev = arr[n-1]
    for i in range(n-1, -1, -1):
        post[i] = min(prev, arr[i])
        prev = post[i]

    for i in range(1, n-1):
        if(arr[i]>=pre[i-1] and arr[i]<=post[i+1]):
            return arr[i]
    
    return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(findElement(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends