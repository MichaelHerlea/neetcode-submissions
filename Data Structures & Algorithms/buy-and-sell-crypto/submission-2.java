class Solution {
    public int maxProfit(int[] prices) {
        int max_profit = 0;
        int i = 0;
        int j = 1;

        while (j < prices.length) {
            max_profit = Math.max(max_profit, prices[j] - prices[i]);

            if (prices[j] < prices[i]) {
                i = j;
            }

            j++;
        }

        return max_profit;
    }
}
