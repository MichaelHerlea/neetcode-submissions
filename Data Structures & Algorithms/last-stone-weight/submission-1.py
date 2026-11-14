import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) >= 2:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            weight_difference = x - y
            if weight_difference != 0:
                heapq.heappush_max(stones, abs(weight_difference))
        
        return heapq.heappop_max(stones) if len(stones) > 0 else 0