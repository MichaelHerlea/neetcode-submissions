class Solution {
    public int climbStairs(int n) {
        Map<Integer, Integer> memo = new HashMap<>();
        return helper(n, memo);
    }

    private int helper(int n, Map<Integer, Integer> memo) {
        if (n == 0) {
            return 1;
        }
        if (n < 0) {
            return 0;
        }
        if (memo.containsKey(n)) {
            return memo.get(n);
        }

        int ways = helper(n - 1, memo) + helper(n - 2, memo);
        memo.put(n, ways);
        return ways;
    }
}
