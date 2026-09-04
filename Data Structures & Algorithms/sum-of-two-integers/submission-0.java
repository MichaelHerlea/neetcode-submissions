class Solution {
    public int getSum(int a, int b) {
        int[] aArray = new int[32];
        int[] bArray = new int[32];
        int[] sumArray = new int[32];

        for (int i = 0; i < 32; i++) {
            aArray[31 - i] = (a & 1);
            bArray[31 - i] = (b & 1);

            a >>>= 1;
            b >>>= 1;
        }

        int carryBit = 0;
        for (int i = 31; i >= 0; i--) {
            int sum = carryBit + aArray[i] + bArray[i];
            if (sum == 3) {
                sumArray[i] = 1;
                carryBit = 1;
            } else if (sum == 2) {
                sumArray[i] = 0;
                carryBit = 1;
            } else if (sum == 1) {
                sumArray[i] = 1;
                carryBit = 0;
            } else {
                sumArray[i] = 0;
                carryBit = 0;
            }
        }

        int result = 0;
        for (int i = 0; i < 32; i++) {
            result = (result << 1) | sumArray[i];
        }

        return result;
    }
}