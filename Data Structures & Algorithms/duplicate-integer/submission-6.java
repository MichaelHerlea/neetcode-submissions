class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> values = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (values.contains(nums[i])) {
                return true;
            }
            values.add(nums[i]);
        }
        return false;
    }
}