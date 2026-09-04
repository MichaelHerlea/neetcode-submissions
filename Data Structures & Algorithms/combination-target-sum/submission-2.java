class Solution {
    private final List<List<Integer>> result = new ArrayList<>();
    private int[] nums;
    private int target;

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        // result = new ArrayList<>();
        this.nums = nums;
        this.target = target;
        dfs(0, new ArrayList<>(), 0);
        return result;
    }

    public void dfs(int index, List<Integer> currentlyVisited, int total){
        if (total == target) {
            result.add(new ArrayList<>(currentlyVisited));
            return;
        }
        if (index >= nums.length || total > target) return;

        currentlyVisited.add(nums[index]);
        dfs(index, currentlyVisited, total + nums[index]);
        currentlyVisited.removeLast();

        dfs(index + 1, currentlyVisited, total);
    }
}
