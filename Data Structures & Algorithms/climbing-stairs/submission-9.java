class Solution {
    HashMap<Integer, Integer> memo = new HashMap<>();

    public int climbStairs(int n) {
        return dfs(n);
    }

    public int dfs(int n) {
        if (n == 0) return 1;
        if (n < 0) return 0;

        if (!memo.containsKey(n)) memo.put(n, dfs(n - 1) + dfs(n - 2));

        return memo.get(n);
    }
}
