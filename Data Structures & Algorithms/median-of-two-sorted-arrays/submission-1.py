class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total_size = len(nums1) + len(nums2)
        half = total_size // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            A_middle = (l + r) // 2
            B_middle = half - A_middle - 2

            A_left = A[A_middle] if A_middle >= 0 else float("-inf")
            A_right = A[A_middle + 1] if (A_middle + 1) < len(A) else float("inf")
            B_left = B[B_middle] if B_middle >= 0 else float("-inf")
            B_right = B[B_middle + 1] if (B_middle + 1) < len(B) else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if total_size % 2 == 1:
                    return min(A_right, B_right)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = A_middle - 1
            else:
                l = A_middle + 1
