class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> result = new HashMap<>();
        for (String s : strs) {
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            String sortedS = new String(charArray);
            result.putIfAbsent(sortedS, new ArrayList<>());
            result.get(sortedS).add(s);
        }
        return new ArrayList<>(result.values());
    }
}
