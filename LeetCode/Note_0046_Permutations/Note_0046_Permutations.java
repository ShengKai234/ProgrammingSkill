import java.util.*;

class Solution {

    private List<List<Integer>> output = new ArrayList<List<Integer>>();
    int[] nums = null;

    public List<List<Integer>> permute(int[] nums) {
        this.nums = nums;
        this.backtracking(0);
        return null;
    }

    public void backtracking(int base_swap_index) {
        if (base_swap_index == nums.length) {
            // my way to copy array
            List<Integer> permutation = new ArrayList<Integer>();
            for(int num: this.nums) {
                permutation.add(num);
            }
            this.output.add(permutation);

            // simple way to copy array
            // this.output.add(new ArrayList<Integer>(nums));
        }

        for (int i = base_swap_index; i < nums.length; i++) {
            this.swap(this.nums, base_swap_index, i);
            // System.out.println(Arrays.toString(this.nums));
            
            backtracking(base_swap_index + 1);
            this.swap(this.nums, base_swap_index, i);
        }

    }

    private void swap(int[] nums, int base_swap_index, int i) {
        int temp = nums[base_swap_index];
        nums[base_swap_index] = nums[i];
        nums[i] = temp;
    }

    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
        Solution solution = new Solution();

        solution.permute(new int[]{1,2,3});
        System.out.println(solution.output);
    }

    public void groupAnagrams(String[] strings) {
    }
}