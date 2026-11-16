class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_nums = []
        for num in nums:
            if len(heap_nums) < k:
                heapq.heappush(heap_nums, num)
            elif num > heap_nums[0]:
                heapq.heappushpop(heap_nums, num)
        return heap_nums[0]