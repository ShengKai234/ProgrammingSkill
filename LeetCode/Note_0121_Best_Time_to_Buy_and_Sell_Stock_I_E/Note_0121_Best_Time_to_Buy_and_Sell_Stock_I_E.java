import java.util.*;

class Solution {

    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int buy = prices[0];

        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < buy) {
                // Update buy price if find lower price
                buy = prices[i];
            }

            int profit = prices[i] - buy;
            maxProfit = Math.max(maxProfit, profit);
        }

        return maxProfit;
    }

    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}