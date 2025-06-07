class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        left=0
        n=len(height)
        right=n-1
        while left<=right:
            curr= min(height[left],height[right]) * (right-left)
            area= max(area,curr)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            
        return area