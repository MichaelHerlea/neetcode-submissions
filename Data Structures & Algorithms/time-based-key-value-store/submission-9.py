class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.hashmap.get(key, [])
        l, r = 0, len(entries) - 1
        output = ""

        while l <= r:
            m = (l + r) // 2
            timestamp_prev, value = entries[m]
            if timestamp_prev <= timestamp:
                output = value
                l = m + 1
            else:
                r = m - 1

        return output
