"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_count = 0
        start_times = []
        end_times = []

        for meeting in intervals:
            start_times.append(meeting.start)
            end_times.append(meeting.end)

        start_times.sort()
        end_times.sort()

        i, j = 0, 0
        while i < len(start_times):
            if start_times[i] < end_times[j]:
                i += 1
            else:
                j += 1
            max_count = max(max_count, i - j)

        return max_count