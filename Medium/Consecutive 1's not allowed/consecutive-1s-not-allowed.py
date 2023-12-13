#User function Template for python3
class Solution:

	def countStrings(self,n):
    	# code here
    	a = 1
    	b = 1 
    	mod = (10**9 + 7)
    	for i in range(n-1):
    	    a, b = (a+b) %mod, a 
    	
    	return (a+b)%mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
# } Driver Code Ends