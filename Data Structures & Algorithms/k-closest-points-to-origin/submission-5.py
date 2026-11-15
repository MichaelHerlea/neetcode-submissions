class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_heap = []
        for point in points:
            if len(points_heap) < k:
                heapq.heappush_max(points_heap, (math.sqrt(point[0]**2 + point[1]**2), point))
            else:
                heapq.heappushpop_max(points_heap, (math.sqrt(point[0]**2 + point[1]**2), point))
        
        output = []
        for _ in range(k):
            output.append(heapq.heappop_max(points_heap)[1])
        
        return output