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

    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}