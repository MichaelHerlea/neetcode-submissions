class Twitter:
    def __init__(self):
        self.followers = defaultdict(set) # FollowerID : [set of followeesID]
        self.tweets = defaultdict(list) # PosterID : [list of tweetID]
        self.tweet_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweet_count, tweetId))
        self.tweet_count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweet_feed = []
        max_heap = []

        self.followers[userId].add(userId)

        for followeeID in self.followers[userId]:
            if followeeID in self.tweets:
                index = len(self.tweets[followeeID]) - 1
                count, tweet_id = self.tweets[followeeID][index]
                max_heap.append((count, tweet_id, followeeID, index - 1))

        heapq.heapify_max(max_heap)

        while max_heap and len(tweet_feed) < 10:
            count, tweet_id, followeeID, index = heapq.heappop_max(max_heap)
            tweet_feed.append(tweet_id)
            if index >= 0:
                count, tweet_id = self.tweets[followeeID][index]
                heapq.heappush_max(max_heap, (count, tweet_id, followeeID, index - 1))

        return tweet_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
