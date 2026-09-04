class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> set_of_visited_numbers = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (set_of_visited_numbers.containsKey(target - nums[i])) {
                return new int[]{set_of_visited_numbers.get(target - nums[i]), i};
            }
            set_of_visited_numbers.put(nums[i], i);
        }
        return null;
    }
}
