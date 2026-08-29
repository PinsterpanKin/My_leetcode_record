class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area
'''
2,1,5,6,2,3
'''

#Time limit exceeded but generate correct answers
class Original:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        summit = max(heights)
        max_area = summit
        max_width = 1
        width = 0
        for height in range(1, summit + 1):
            for i in range(length):
                if heights[i] >= height:
                    width += 1
                else:
                    width = 0
                max_width = max(max_width, width)
            max_area = max(max_area, height * max_width)
            max_width = 1
            width = 0
        return max_area