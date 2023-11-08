class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x_dist = abs(fx-sx)
        y_dist = abs(fy-sy) 
        range = max(x_dist, y_dist)

        if x_dist == 0 and y_dist == 0 and t==1:
            return False 
        
        return t>=range