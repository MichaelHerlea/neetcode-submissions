"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        previous_end_time = 0
        for i in range(len(intervals)):
            if intervals[i].start < previous_end_time:
                return False
            previous_end_time = intervals[i].end
        return True;