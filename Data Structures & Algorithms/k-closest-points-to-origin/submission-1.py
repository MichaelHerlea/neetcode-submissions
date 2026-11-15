import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_heap = []
        for point in points:
            heapq.heappush(points_heap, (math.sqrt(point[0]**2 + point[1]**2), point))
        
        output = []
        for _ in range(k):
            distance, point = heapq.heappop(points_heap)
            output.append(point)
        
        return output