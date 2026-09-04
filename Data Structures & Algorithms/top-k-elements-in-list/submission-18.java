class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> frequency_of_characters = new HashMap<>();
        for (int i : nums) {
            frequency_of_characters.put(i, frequency_of_characters.getOrDefault(i, 0) + 1);
        }

        ArrayList<Map.Entry<Integer, Integer>> sorted_characters = new ArrayList<>(frequency_of_characters.entrySet());
        sorted_characters.sort((a, b) -> b.getValue() - a.getValue());

        int[] result_set = new int[k];
        for (int i = 0; i < k; i++) {
            result_set[i] = sorted_characters.get(i).getKey().intValue();
        }
        return result_set;
    }
}
