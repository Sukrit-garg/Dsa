class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        if len(heights)==1:
            return heights[0]
        max_rect = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                ind= stack.pop()
                w=i if not stack else i-stack[-1]-1
                max_rect = max(max_rect, heights[ind]*(w))
            stack.append(i)
        return max_rect