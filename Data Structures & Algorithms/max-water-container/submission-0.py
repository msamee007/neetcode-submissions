class Solution(object):
    def maxArea(self, height):
        max_water=0
        l,r=0,len(height)-1
        while(l<r):
            area=(r-l)*(min(height[l],height[r]))
            if area>max_water:
                max_water=area
            if(height[l]<height[r]):
             l+=1
            else:
                r-=1
        return max_water