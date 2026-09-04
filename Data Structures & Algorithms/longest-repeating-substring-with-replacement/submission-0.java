class Solution {
    public int characterReplacement(String s, int k) {
        int result = 0;
        int left = 0;
        HashMap<Character, Integer> characters = new HashMap<>();

        for (int right = 0; right < s.length(); right++) {
            characters.merge(s.charAt(right), 1, Integer::sum);

            while (right - left + 1 - Collections.max(characters.values()) > k) {
                characters.merge(s.charAt(left), -1, Integer::sum);
                left++;
            }

            result = Math.max(result, right - left + 1);
        }

        return result;
    }
}
