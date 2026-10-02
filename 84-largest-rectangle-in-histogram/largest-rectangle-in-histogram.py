class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        area = 0
        stack = []
        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][0]:
                height, start = stack.pop()
                width = i - start
                area = max(area,height*width)
            stack.append((heights[i], start))
        i = len(heights)
        while stack :
            height,start = stack.pop()
            width = i - start
            area = max(area,height*width)
        return area 