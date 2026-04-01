class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointer solution, i , j
        res = 0

        if not height:
            return res


        for i in range(len(height)):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(height[j], leftMax)

            for j in range(i+1, len(height)):
                rightMax = max(height[j], rightMax)

            res += min(leftMax, rightMax) - height[i] 

        return res
        
        