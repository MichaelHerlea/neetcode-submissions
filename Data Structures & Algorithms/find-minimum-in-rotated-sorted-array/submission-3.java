class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int middle = nums.length / 2;
        int result = nums[0];
        
        while (left <= right) {
            if (nums[left] <= nums[right]) {
                result = Math.min(result, nums[left]);
                break;
            }

            middle = (left + right) / 2;
            result = Math.min(result, nums[middle]);

            if (nums[left] <= nums[middle]) {
                left = middle + 1;
            }
            else {
                right = middle;
            }
        }
        return result;
    }
}
