class Solution {
    public int[] countBits(int n) {
        int[] output = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            int value = 0;
            int k = i;
            for (int j = 0; j < 32; j++) {
                if ((k & 1) == 1) {
                    value++;
                }
                k = k >> 1;
            }
            output[i] = value;
        }

        return output;
    }
}
