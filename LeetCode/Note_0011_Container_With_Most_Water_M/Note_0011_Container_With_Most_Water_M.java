import java.util.*;

class Solution {

    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;

        int max_area = 0;
        while (left < right) {
            int h = Math.min(height[left], height[right]);
            int area = h * (right - left);
            max_area = Math.max(max_area, area);
            if (height[left] <= height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return max_area;
    }

    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}