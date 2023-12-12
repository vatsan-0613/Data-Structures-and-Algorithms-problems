import math
class Solution:
    def isPrime (self, N):
        # code here
        if(N==1):
            return 0
        prime = 1
        for i in range(2, int(math.sqrt(N))+1):
            if(N%i == 0):
                prime = 0
                break 
        return prime  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends