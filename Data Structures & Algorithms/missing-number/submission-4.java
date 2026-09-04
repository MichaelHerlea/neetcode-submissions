class Solution {
    public int missingNumber(int[] nums) {
        boolean[] presentNumbers = new boolean[nums.length + 1];

        for (int i = 0; i < nums.length; i++) {
            int number = nums[i];
            presentNumbers[number] = true;
        }

        for (int i = 0; i < presentNumbers.length; i++) {
            if (presentNumbers[i] == false) {
                return i;
            }
        }
        return 0;
    }
}
