class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> data_hashSet = new HashSet();
        
        for (int i = 0; i < nums.length; i++) {
            data_hashSet.add(nums[i]);
        }

        ArrayList<Integer> candidate_starting_numbers = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (!data_hashSet.contains(nums[i] - 1)) {
                candidate_starting_numbers.add(nums[i]);
            }
        }

        int max_length = 0;
        int current_length = 0;
        for (int i = 0; i < candidate_starting_numbers.size(); i++) {
            current_length = 0;

            while (data_hashSet.contains(candidate_starting_numbers.get(i) + current_length)) {
                current_length++;
            }

            max_length = Math.max(max_length, current_length);
        }

        return max_length;
    }
}
