class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix_array = new int[nums.length];
        int[] suffix_array = new int[nums.length];
        int[] result_array = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                prefix_array[i] = nums[i];
            }
            else {
                prefix_array[i] = prefix_array[i - 1] * nums[i];
            }
        }

        for (int i = nums.length - 1; i > 0; i--) {
            if (i == nums.length - 1) {
                suffix_array[i] = nums[i];
            }
            else {
                suffix_array[i] = suffix_array[i + 1] * nums[i];
            }
        }

        for (int i = 0; i < result_array.length; i++) {
            if (i == 0) {
                result_array[i] = suffix_array[i + 1];
            }
            else if (i ==  result_array.length - 1) {
                result_array[i] = prefix_array[i - 1];
            }
            else {
                result_array[i] = prefix_array[i - 1] * suffix_array[i + 1];
            }
        }

        return result_array;
    }
}  
