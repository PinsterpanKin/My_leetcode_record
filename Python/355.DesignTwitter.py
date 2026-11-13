class MyTwitter:

    def __init__(self):
        from collections import defaultdict
        self.feed = []
        self.relation = defaultdict(set)
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for uid, tid in reversed(self.feed):
            if uid == userId or uid in self.relation[userId]:
                res.append(tid)
            if len(res) == 10:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.relation[followerId]:
            self.relation[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.relation[followerId]:
            self.relation[followerId].remove(followeeId)

# Best Implementation
from collections import defaultdict, deque
from heapq import merge
from itertools import islice
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(lambda: deque(maxlen=10))
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].appendleft((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        streams = [self.tweets[u] for u in users if u in self.tweets]
        return [tid for _, tid in islice(merge(*streams, reverse=True), 10)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)