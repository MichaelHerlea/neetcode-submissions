class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if (c == '(' ||
                c == '{' ||
                c == '[') {
                    stack.push(c);
            }
            else if (c == ')' && (stack.size() == 0 || stack.pop() != '(')) {
                return false;
            }
            else if (c == '}' && (stack.size() == 0 || stack.pop() != '{')) {
                return false;
            }
            else if (c == ']' && (stack.size() == 0 || stack.pop() != '[')) {
                return false;
            }
        }

        return (stack.size() == 0);
    }
}
