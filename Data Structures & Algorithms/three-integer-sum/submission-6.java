class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> output = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i - 1] == nums[i]) {
                continue;
            }

            int j = i + 1;
            int k = nums.length - 1;

            while (j < k) {
                if (nums[i] + nums[j] + nums[k] == 0) {
                    ArrayList<Integer> temp_var = new ArrayList<>();
                    temp_var.add(nums[i]);
                    temp_var.add(nums[j]);
                    temp_var.add(nums[k]);
                    output.add(temp_var);
                    j++;
                    k--;

                    while (j < k && nums[j] == nums[j - 1]) {
                        j++;
                    }
                    while (j < k && nums[k] == nums[k + 1]) {
                        k--;
                    }
                }
                else if (nums[i] + nums[j] + nums[k] > 0) {
                    k--;
                }
                else {
                    j++;
                }
            }
        }

        return output;
    }
}
