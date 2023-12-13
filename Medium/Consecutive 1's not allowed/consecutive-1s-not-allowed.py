#User function Template for python3
class Solution:

	def countStrings(self,n):
    	# code here
    	if n == 1:
            return 2
        elif n == 2:
            return 3
    
        dp = [0] * (n + 1)
        dp[1] = 2
        dp[2] = 3
    
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2])%(10**9+7)
    
        return dp[n]%(10**9+7)


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