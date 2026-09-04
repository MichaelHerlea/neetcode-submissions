class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int max_length = 0;
        HashSet<Character> characters = new HashSet<>();

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);

            if (characters.contains(c)) {
                while (s.charAt(left) != c) {
                    characters.remove(s.charAt(left));
                    left++;
                }
                characters.remove(s.charAt(left));
                left++;
            }

            characters.add(c);
            max_length = Math.max(max_length, right - left + 1);
        }

        return max_length;
    }
}
