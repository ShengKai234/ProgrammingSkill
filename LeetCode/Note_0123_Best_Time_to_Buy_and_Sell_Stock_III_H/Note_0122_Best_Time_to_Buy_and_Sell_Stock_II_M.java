import java.util.*;

class Solution {

    public int maxProfit_by_valleypeak(int[] prices) {
        // valley, peak approuch
        int total = 0;
        int valley = Integer.MAX_VALUE;
        int peak = valley;

        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < peak) {
                // find lower price than peak
                // record profit
                total += peak - valley;
                
                // update valley
                valley = prices[i];
                peak = valley;
            } else {
                // find higher price than peak
                // update peak (bigger price)
                peak = prices[i];
            }
        }

        // remember calculate final round
        total += peak - valley;
        
        return total;
    }

    public int maxProfit_by_onepass(int[] prices) {
        // one pass
        int total = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {
                total += prices[i] - prices[i - 1];
            }
        }

        return total;
    }

    public int maxProfit_by_dp(int[] prices) {
        int[] res = dp(prices.length - 1, prices);
        return res[1];
    }

    public int[] dp(int day, int[] prices) {
        if (day == 0) {
            // {hold, not hold}
            int[] res = new int[]{-prices[day], 0};
            return res;
        }

        int[] pre = dp(day - 1, prices);
        int preHold = pre[0];
        int preNotHold = pre[1];
        int hold = Math.max(preHold, preNotHold - prices[day]);
        int notHold = Math.max(preNotHold, preHold + prices[day]);

        return new int[]{hold, notHold};
    }

    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}