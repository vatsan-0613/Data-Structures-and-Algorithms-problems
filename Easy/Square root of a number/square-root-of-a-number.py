#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x): 
    #Your code here
        low = 1 
        high = x 
        res = 1
        while(low<=high):
            mid = (low+high)//2
            if(mid*mid == x):
                return mid 
            if(mid*mid < x):
                low = mid+1 
                res = mid
            else:
                high = mid-1 
        
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends