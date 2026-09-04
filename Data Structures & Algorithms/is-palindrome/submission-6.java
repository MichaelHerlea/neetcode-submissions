class Solution {
    public boolean isPalindrome(String s) {
        if (s.length() <= 1) {
            return true;
        }

        int i = 0;
        int j = s.length() - 1;

        while (i < j) {
            if (!(Character.isLetter(s.charAt(i)) || Character.isDigit(s.charAt(i)))) {
                i++;
            }
            else if (!(Character.isLetter(s.charAt(j)) || Character.isDigit(s.charAt(j)))) {
                j--;
            }
            else if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) {
                return false;
            }
            else {
                i++;
                j--;
            }
        }
        return true;
    }
}
