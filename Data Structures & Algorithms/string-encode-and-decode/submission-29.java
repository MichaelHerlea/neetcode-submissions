class Solution {

    public String encode(List<String> strs) {
        StringBuilder result_string = new StringBuilder();

        for (String s : strs) {
            result_string.append(s.length() + ",");
        }
        result_string.append('#');
        for(String s : strs) {
            result_string.append(s);
        }

        return result_string.toString();
    }

    public List<String> decode(String str) {
        ArrayList<Integer> string_length = new ArrayList<>();
        ArrayList<String> result_list = new ArrayList<>();

        int start_index = 0;
        int end_index = 0;
        while (str.charAt(end_index) != '#') {
            if (str.charAt(end_index) == ',') {
                string_length.add(Integer.parseInt(str.substring(start_index ,end_index)));
                start_index = end_index + 1;
            }
            end_index++;
        }
        start_index = end_index + 1;

        for (Integer length : string_length) {
            result_list.add(str.substring(start_index, start_index + length));
            start_index += length;
        }

        return result_list;
    }
}
