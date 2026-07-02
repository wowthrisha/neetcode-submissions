class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        l=0
        r=len(heights)-1
        while l<r:
            a=min(heights[l],heights[r])
            
            w=r-l
            area=w*a
            if area>max_area:
                max_area=area
            if a==heights[l]:
                l+=1
            else:
                r-=1
        return max_area

        