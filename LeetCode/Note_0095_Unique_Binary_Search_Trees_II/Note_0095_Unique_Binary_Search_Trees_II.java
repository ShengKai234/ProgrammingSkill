import java.util.*;



class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) {
            this.val = val;
        }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public List<TreeNode> generateTrees(int n) {
        return rec(1, n);
    }

    public List<TreeNode> rec(int start, int end) {
        if (start > end) {
            List<TreeNode> r = new ArrayList<TreeNode>();
            r.add(null);
            return r;
        }

        List<TreeNode> all_trees = new ArrayList<TreeNode>();
        for (int i = start; i < end + 1; i++) {
            // left
            List<TreeNode> left_trees = rec(start, i - 1);

            // right
            List<TreeNode> right_trees = rec(i + 1, end);

            for (TreeNode left_node: left_trees) {
                for (TreeNode right_node: right_trees) {
                    TreeNode current_node = new TreeNode(i, left_node, right_node);
                    all_trees.add(current_node);
                }
            }
        }
        return all_trees;
    }

    public void print_node(TreeNode node) {
        Queue<TreeNode> q = new LinkedList<>();
        q.add(node);
        while (q.size() > 0) {
            for (int i = 0; i < q.size(); i++) {
                TreeNode pop_node = q.poll();
                if (pop_node == null) {
                    System.out.print(null + " ");
                    continue;
                }
                System.out.print(pop_node.val + " ");
                q.add(pop_node.left);
                q.add(pop_node.right);
            }
        }
    }

    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
        Solution solution = new Solution();
        List<TreeNode> res = solution.generateTrees(3);
        System.out.println(res.size());
        for (TreeNode node: res) {
            System.out.println(" ");
            solution.print_node(node);
        }
    }
}