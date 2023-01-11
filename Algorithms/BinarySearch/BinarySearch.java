package Algorithms.BinarySearch;

import java.util.List;

public class BinarySearch {

    private int binarySearch(int[] nums, int target) {
        System.out.println("Start Search ...");
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = (right - left) / 2 + left;
            
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            }
        }

        return -1;
    }


    public static void main(String[] args) {
        System.out.println("Binary Search !");

        int[] nums = {1,3,4,71,400,100};
        int target = 4;
        BinarySearch solution = new BinarySearch();
        System.out.println(solution.binarySearch(nums, target));

        target = 5;
        System.out.println(solution.binarySearch(nums, target));
    }
}
