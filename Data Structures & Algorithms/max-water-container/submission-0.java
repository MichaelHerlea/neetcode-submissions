class Solution {
    public int maxArea(int[] heights) {
        int max_area = 0;
        int i = 0;
        int j = heights.length - 1;

        while (i < j) {
            max_area = Math.max(max_area, (j - i) * Math.min(heights[i], heights[j]));

            if (heights[i] < heights[j]) {
                i++;
            }
            else if (heights[i] > heights[j]) {
                j--;
            }
            else {
                i++;
            }
        }

        return max_area;
    }
}
