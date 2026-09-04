class Solution {
    public String minWindow(String s, String t) {
        int left = 0;
        int minSizeValidSubstring = Integer.MAX_VALUE;
        String minValidSubstring = new String();

        HashMap<Character, Integer> sCharacterCounter = new HashMap<>();
        HashMap<Character, Integer> tCharacterCounter = new HashMap<>();

        for (int i = 0; i < t.length(); i++) {
            tCharacterCounter.merge(t.charAt(i), 1, Integer::sum);
        }

        for (int right = 0; right < s.length(); right++) {
            sCharacterCounter.merge(s.charAt(right), 1, Integer::sum);

            while (checkIfValid(sCharacterCounter, tCharacterCounter)) {
                if (minSizeValidSubstring > right - left + 1) {
                    minSizeValidSubstring = right - left + 1;
                    minValidSubstring = s.substring(left, right + 1);
                }
                sCharacterCounter.merge(s.charAt(left), -1, Integer::sum);
                left++;
            }
        }
        return minValidSubstring;
    }

    public boolean checkIfValid(HashMap<Character, Integer> sCharacterCounter, HashMap<Character, Integer> tCharacterCounter) {
        boolean isValid = true;
        for (Character keyValue : tCharacterCounter.keySet()) {
            if (tCharacterCounter.get(keyValue) > sCharacterCounter.getOrDefault(keyValue, 0)) {
                isValid = false;
            }
        }
        return isValid;
    }
}
