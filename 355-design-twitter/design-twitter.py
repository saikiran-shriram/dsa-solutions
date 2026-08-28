class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.count += 1
        self.tweets[userId].append((tweetId,self.count))

    def getNewsFeed(self, userId: int) -> List[int]:
        post = [] 
        if userId in self.tweets:
            post.extend(self.tweets[userId])
        if userId in self.followers :
            for value in self.followers[userId] :
                if value in self.tweets : 
                    post.extend(self.tweets[value])
        post = sorted(post, key=lambda x: x[1], reverse=True)
        return [x[0] for x in post[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = []
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers :
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)