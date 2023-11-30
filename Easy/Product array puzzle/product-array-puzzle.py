#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        
        if(n==1): return [1]
        
        res = [1 for _ in range(n)]
        
        temp = 1
        for i in range(0, n):
            res[i] = temp
            temp *= nums[i]
        
        temp = 1
        for i in range(n-1, -1, -1):
            res[i]*=temp
            temp *= nums[i]
            
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends