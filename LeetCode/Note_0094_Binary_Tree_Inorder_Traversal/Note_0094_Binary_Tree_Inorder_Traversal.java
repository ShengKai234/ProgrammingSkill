import java.util.*;


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    List<Integer> output = new ArrayList<>();

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        this.helper(root);
        return this.output;
    }

    public void helper(TreeNode root) {
        if (root == null) {
            return;
        }

        this.helper(root.left);
        this.output.add(root.val);
        this.helper(root.right);
    }

    public static void main(String[] args) {
        System.out.println("Note_0094_Binary_Tree_Inorder_Traversal!"); 
        TreeNode node2 = new TreeNode(3, null, null);
        TreeNode node1 = new TreeNode(2, node2, null);
        TreeNode root = new TreeNode(1, null, node1);
        
        Solution solution = new Solution();
        solution.inorderTraversal(root);
        System.out.println(solution.output);
    }
}