#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        # code here
        for num in array:
            ind = abs(num)-1 
            if(ind==n-1):
                continue
            array[ind] = -1*array[ind] 
            
        for ind, num in enumerate(array):
            if(num>0):
                return ind+1 
        
        return n
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends