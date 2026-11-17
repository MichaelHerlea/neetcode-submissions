class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = list(count.values())
        heapq.heapify_max(max_heap)
        queue = deque() # (count, time)
        time = 0

        while max_heap or queue:
            time += 1
            if max_heap:
                count = heapq.heappop_max(max_heap) - 1
                if count:
                    queue.append((count, time + n))

            if queue and queue[0][1] <= time:
                heapq.heappush_max(max_heap, queue.popleft()[0])

        return time
