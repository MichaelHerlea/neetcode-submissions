class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> s_HashTable = new HashMap<>();
        HashMap<Character, Integer> t_HashTable = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            s_HashTable.merge(s.charAt(i), 1, Integer::sum);
        }

        for (int i = 0; i < t.length(); i++) {
            t_HashTable.merge(t.charAt(i), 1, Integer::sum);
        }

        return s_HashTable.equals(t_HashTable);
    }
}
