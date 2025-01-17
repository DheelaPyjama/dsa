# container with max water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        res=0
        while l<r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l+=1
            else: 
                r-=1
        return res
    
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
    
