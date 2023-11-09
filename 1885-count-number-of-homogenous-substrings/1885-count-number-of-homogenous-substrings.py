class Solution:
    def countHomogenous(self, s: str) -> int:
        
        i = 0
        res = 0
        while(i<len(s)):
            count = 0
            l = s[i]
            while(i<len(s) and s[i]==l):
                count += 1
                i+=1
            res+=(count * (count+1))//2
            print(count)
        
        return res%(10**9+7)
            
        