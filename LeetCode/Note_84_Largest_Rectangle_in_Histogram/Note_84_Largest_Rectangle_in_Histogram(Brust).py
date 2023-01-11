class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        _max = 0

        for i in range(n):
            print("curr: ",i)
            left, right = i, i

            while left > 0:
                if heights[left - 1] >= heights[i]:
                    left -= 1
                else:
                    break

            while right < n - 1:
                if heights[right + 1] >= heights[i]:
                    right += 1
                else:
                    break
            
            area = heights[i] * (right - left + 1)
            print(left, right, area)
            if area > _max:
                _max = area

        return _max
   

if __name__ == '__main__':
    print("template")
    solution = Solution()

# T:O(n)
# S:O(n)