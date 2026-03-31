class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxArea = 0
        #[1,7,2,5,4,7,3,6]
        # l             r
        while l < r:
            #      8       * 
            area = ((r - l) * min(heights[r], heights[l]))
            maxArea = max(area, maxArea)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxArea
