class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sliding_window_deque = []
        output = []

        for index in range(k):
            while sliding_window_deque and sliding_window_deque[-1] < nums[index]:
                sliding_window_deque.pop()
            sliding_window_deque.append(nums[index])
        output.append(sliding_window_deque[0])
        
        for index in range(k, len(nums)):
            if sliding_window_deque[0] == nums[index - k]: sliding_window_deque.remove(nums[index - k])

            while sliding_window_deque and sliding_window_deque[-1] < nums[index]:
                sliding_window_deque.pop()
            sliding_window_deque.append(nums[index])

            output.append(sliding_window_deque[0])
        
        return output